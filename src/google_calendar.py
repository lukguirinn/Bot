

"""
Gestiona el acceso a Google Calendar de cada usuario.
"""

import json
import os

from cryptography.fernet import Fernet
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth.exceptions import RefreshError
from googleapiclient.discovery import build

from src.database import obtener_conexion, guardar_conexion


SCOPES = [
    "https://www.googleapis.com/auth/calendar.events"
]


def obtener_cifrador():
    """
    Crea el cifrador de credenciales.

    Retorno:
        Fernet: Objeto de cifrado.
    """

    clave = os.getenv("GOOGLE_TOKEN_ENCRYPTION_KEY")

    if not clave:
        raise ValueError("Falta GOOGLE_TOKEN_ENCRYPTION_KEY")

    return Fernet(clave.encode())


def obtener_credenciales(telefono: str):
    """
    Recupera, descifra y renueva las credenciales de un usuario.

    Parámetros:
        telefono (str): Número de WhatsApp.

    Retorno:
        Credentials | None: Credenciales de Google.
    """

    credenciales_cifradas = obtener_conexion(telefono)

    if not credenciales_cifradas:
        return None

    cifrador = obtener_cifrador()

    credenciales_json = cifrador.decrypt(
        credenciales_cifradas.encode()
    ).decode()

    datos = json.loads(credenciales_json)

    credenciales = Credentials.from_authorized_user_info(
        datos,
        SCOPES
    )

    if credenciales.expired and credenciales.refresh_token:

        try:
            credenciales.refresh(Request())

            nuevas_credenciales = cifrador.encrypt(
                credenciales.to_json().encode()
            ).decode()

            guardar_conexion(
                telefono,
                nuevas_credenciales
            )

        except RefreshError:
            return None

    return credenciales


def obtener_servicio_calendario(telefono: str):
    """
    Construye el servicio de Google Calendar de un usuario.

    Parámetros:
        telefono (str): Número de WhatsApp.

    Retorno:
        Resource | None: Servicio de Google Calendar.
    """

    credenciales = obtener_credenciales(telefono)

    if not credenciales or not credenciales.valid:
        return None

    servicio = build(
        "calendar",
        "v3",
        credentials=credenciales
    )

    return servicio


def validar_calendario(telefono: str):
    """
    Valida el acceso del usuario a Google Calendar.

    Parámetros:
        telefono (str): Número de WhatsApp.

    Retorno:
        dict: Estado de conexión y datos disponibles.
    """

    servicio = obtener_servicio_calendario(telefono)

    if not servicio:
        return {
            "error": "El usuario no tiene una conexión válida"
        }

    calendario = servicio.events().list(
        calendarId="primary",
        maxResults=1
    ).execute()

    return {
        "conectado": True,
        "nombre": calendario.get("summary"),
        "zona_horaria": calendario.get("timeZone")
    }
