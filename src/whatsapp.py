
"""
Contiene las funciones para comunicarse con la API de WhatsApp.
"""

import os
import requests

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")


def enviar_plantilla(destinatario: str, plantilla: str, idioma: str = "en_US") -> dict:
    """
    Envía una plantilla aprobada de WhatsApp.

    Parámetros:
        destinatario (str): Número del destinatario.
        plantilla (str): Nombre de la plantilla aprobada.
        idioma (str): Idioma de la plantilla.

    Retorno:
        dict: Resultado de la solicitud a la API.
    """

    if not TOKEN or not PHONE_NUMBER_ID:
        return {"error": "Faltan las credenciales de WhatsApp"}

    url = f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/messages"

    encabezados = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    datos = {
        "messaging_product": "whatsapp",
        "to": destinatario,
        "type": "template",
        "template": {
            "name": plantilla,
            "language": {
                "code": idioma
            }
        }
    }

    try:
        respuesta = requests.post(
            url,
            headers=encabezados,
            json=datos,
            timeout=20
        )

        try:
            contenido = respuesta.json()
        except ValueError:
            contenido = {"respuesta": respuesta.text}

        return {
            "status": respuesta.status_code,
            "respuesta": contenido
        }

    except requests.RequestException as error:
        return {"error": str(error)}
