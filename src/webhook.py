
"""
Gestiona las solicitudes entrantes del webhook de WhatsApp.
"""

import os

from flask import Flask, request

from src.bot import procesar_mensaje
from src.whatsapp import enviar_plantilla
from src.google_auth import google_bp, desconectar_google


app = Flask(__name__)

VERIFY_TOKEN = os.getenv("WEBHOOK_VERIFY_TOKEN")

PLANTILLAS = {
    "saludo": "hello_world"
}

app.register_blueprint(google_bp)


def es_solicitud_desconexion(texto: str) -> bool:
    """
    Identifica si el usuario solicita desconectar Google.

    Parámetros:
        texto (str): Mensaje recibido por WhatsApp.

    Retorno:
        bool: True si solicita desconectarse.
    """

    texto = texto.lower().strip()

    solicitudes = [
        "desconectar google",
        "desconectar mi google",
        "desvincular google",
        "desvincular mi calendario",
        "desconectar calendario",
        "desconectar mi cuenta"
    ]

    return texto in solicitudes


@app.route("/webhook", methods=["GET"])
def verificar_webhook():
    """
    Verifica el webhook con Meta.

    Retorno:
        str: Desafío de verificación o mensaje de error.
    """

    modo = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    desafio = request.args.get("hub.challenge")

    if modo == "subscribe" and token == VERIFY_TOKEN:
        return desafio, 200

    return "Error de verificación", 403


@app.route("/webhook", methods=["POST"])
def recibir_mensaje():
    """
    Recibe y procesa mensajes de WhatsApp.

    Retorno:
        str: Confirmación de recepción.
    """

    datos = request.get_json(silent=True)

    if not datos:
        return "EVENT_RECEIVED", 200

    try:
        mensajes = datos["entry"][0]["changes"][0]["value"]["messages"]

        for mensaje_recibido in mensajes:

            remitente = mensaje_recibido["from"]

            if mensaje_recibido["type"] == "text":

                texto = mensaje_recibido["text"]["body"]

                print("Remitente:", remitente)
                print("Mensaje:", texto)

                if es_solicitud_desconexion(texto):

                    resultado = desconectar_google(remitente)

                    print("Resultado de desconexión:", resultado)

                    continue

                resultado = procesar_mensaje(texto, remitente)

                print("Resultado:", resultado)

                if resultado in PLANTILLAS:

                    plantilla = PLANTILLAS[resultado]

                    respuesta = enviar_plantilla(
                        remitente,
                        plantilla
                    )

                    print("Respuesta de WhatsApp:", respuesta)

                else:
                    print("Todavía no hay una plantilla asignada.")

    except (KeyError, IndexError, TypeError):
        print("Notificación sin mensaje procesable.")

    except Exception:
        app.logger.exception(
            "Error procesando el mensaje de WhatsApp"
        )

    return "EVENT_RECEIVED", 200
