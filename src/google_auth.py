
"""
Gestiona la autenticación OAuth de Google Calendar.
"""

import os
import requests

from cryptography.fernet import Fernet
from flask import Blueprint, redirect, request, current_app
from google_auth_oauthlib.flow import Flow
from itsdangerous import (
    URLSafeTimedSerializer,
    BadSignature,
    SignatureExpired
)

from src.database import (
    inicializar_db,
    guardar_conexion,
    eliminar_conexion
)

from src.google_calendar import obtener_credenciales


google_bp = Blueprint("google", __name__)


CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
ENCRYPTION_KEY = os.getenv("GOOGLE_TOKEN_ENCRYPTION_KEY")


if os.getenv("FLASK_ENV") == "development":
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


SCOPES = [
    "https://www.googleapis.com/auth/calendar.events"
]


def obtener_firmador():
    """
    Crea el firmador de enlaces OAuth.

    Retorno:
        URLSafeTimedSerializer: Firmador de seguridad.
    """

    if not FLASK_SECRET_KEY:
        raise ValueError("Falta FLASK_SECRET_KEY")

    return URLSafeTimedSerializer(FLASK_SECRET_KEY)


def obtener_cifrador():
    """
    Crea el cifrador de credenciales.

    Retorno:
        Fernet: Objeto de cifrado.
    """

    if not ENCRYPTION_KEY:
        raise ValueError("Falta GOOGLE_TOKEN_ENCRYPTION_KEY")

    return Fernet(ENCRYPTION_KEY.encode())


def crear_enlace_conexion(telefono: str) -> str:
    """
    Genera un enlace individual de autorización.

    Parámetros:
        telefono (str): Número de WhatsApp del usuario.

    Retorno:
        str: Enlace para iniciar OAuth.
    """

    if not telefono or not telefono.isdigit():
        raise ValueError("Número de WhatsApp inválido")

    if not REDIRECT_URI:
        raise ValueError("Falta GOOGLE_REDIRECT_URI")

    token = obtener_firmador().dumps({
        "telefono": telefono
    })

    base_url = REDIRECT_URI.rsplit("/oauth/callback", 1)[0]

    return f"{base_url}/google/conectar/{token}"


def crear_flujo_oauth(state=None):
    """
    Configura el flujo OAuth de Google.

    Parámetros:
        state (str): Estado de autorización.

    Retorno:
        Flow: Flujo OAuth configurado.
    """

    if not CLIENT_ID or not CLIENT_SECRET or not REDIRECT_URI:
        raise ValueError("Faltan las credenciales OAuth de Google")

    configuracion = {
        "web": {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": [REDIRECT_URI]
        }
    }

    flujo = Flow.from_client_config(
        configuracion,
        scopes=SCOPES,
        state=state,
        redirect_uri=REDIRECT_URI,
        autogenerate_code_verifier=False
    )

    return flujo


@google_bp.route("/google/conectar/<token>")
def conectar_google(token):
    """
    Inicia la autorización de Google para un usuario.
    """

    try:
        datos = obtener_firmador().loads(
            token,
            max_age=600
        )

        telefono = datos["telefono"]

        if not telefono.isdigit():
            return "Número de WhatsApp inválido", 400

    except (BadSignature, SignatureExpired, KeyError, TypeError):
        return "Enlace inválido o vencido", 400

    try:
        flujo = crear_flujo_oauth()

        state = obtener_firmador().dumps({
            "telefono": telefono
        })

        url, _ = flujo.authorization_url(
            access_type="offline",
            include_granted_scopes="true",
            prompt="consent",
            state=state
        )

        return redirect(url)

    except Exception:
        current_app.logger.exception(
            "Error iniciando la autorización de Google"
        )

        return "No se pudo iniciar la conexión con Google", 500


@google_bp.route("/oauth/callback")
def oauth_callback():
    """
    Recibe la autorización de Google y guarda las credenciales.
    """

    if request.args.get("error"):
        current_app.logger.warning(
            "El usuario canceló o rechazó la autorización OAuth"
        )

        return "El usuario rechazó o canceló la autorización", 400

    state = request.args.get("state")

    if not state:
        return "Falta el estado de autorización", 400

    try:
        datos = obtener_firmador().loads(
            state,
            max_age=600
        )

        telefono = datos["telefono"]

        if not telefono.isdigit():
            return "Número de WhatsApp inválido", 400

        flujo = crear_flujo_oauth(state=state)

        flujo.fetch_token(
            authorization_response=request.url
        )

        credenciales = flujo.credentials

        if not credenciales.refresh_token:
            current_app.logger.warning(
                "Google no devolvió un refresh token"
            )

        credenciales_json = credenciales.to_json()

        credenciales_cifradas = obtener_cifrador().encrypt(
            credenciales_json.encode()
        ).decode()

        inicializar_db()

        guardar_conexion(
            telefono,
            credenciales_cifradas
        )

        return "Google Calendar conectado correctamente con Calendi."

    except (BadSignature, SignatureExpired, KeyError, TypeError, ValueError):
        current_app.logger.exception(
            "Error validando el estado o la configuración OAuth"
        )

        return "Error al validar la autorización de Google", 400

    except Exception:
        current_app.logger.exception(
            "Error inesperado durante el callback OAuth"
        )

        return "No se pudo completar la conexión con Google", 500


def desconectar_google(telefono: str) -> dict:
    """
    Revoca el acceso de Google y elimina la conexión del usuario.

    Parámetros:
        telefono (str): Número de WhatsApp del usuario.

    Retorno:
        dict: Resultado de la desconexión.
    """

    if not telefono or not telefono.isdigit():
        return {
            "desconectado": False,
            "error": "Número de WhatsApp inválido"
        }

    try:
        credenciales = obtener_credenciales(telefono)

    except Exception:
        current_app.logger.exception(
            "No se pudieron recuperar las credenciales del usuario"
        )

        return {
            "desconectado": False,
            "error": "No se pudieron recuperar las credenciales"
        }

    if not credenciales:
        eliminar_conexion(telefono)

        return {
            "desconectado": True,
            "mensaje": "El usuario ya no tenía una conexión activa"
        }

    token = credenciales.refresh_token or credenciales.token

    if not token:
        return {
            "desconectado": False,
            "error": "No hay un token disponible para revocar"
        }

    try:
        respuesta = requests.post(
            "https://oauth2.googleapis.com/revoke",
            data={"token": token},
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            },
            timeout=15
        )

    except requests.RequestException:
        current_app.logger.exception(
            "No se pudo contactar con Google para revocar el acceso"
        )

        return {
            "desconectado": False,
            "revocacion_google": False,
            "error": "No se pudo contactar con Google"
        }

    if respuesta.status_code != 200:
        current_app.logger.error(
            "Google rechazó la revocación. Código HTTP: %s",
            respuesta.status_code
        )

        return {
            "desconectado": False,
            "revocacion_google": False,
            "error": "Google no confirmó la revocación"
        }

    try:
        eliminar_conexion(telefono)

    except Exception:
        current_app.logger.exception(
            "Google revocó el acceso, pero no se pudo eliminar la conexión local"
        )

        return {
            "desconectado": False,
            "revocacion_google": True,
            "error": "Revocación exitosa, pero falló la eliminación local"
        }

    return {
        "desconectado": True,
        "revocacion_google": True
    }
