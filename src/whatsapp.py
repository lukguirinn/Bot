import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")


def enviar_plantilla(destinatario, plantilla, idioma="es"):
    """
    Envía un mensaje mediante una plantilla aprobada de WhatsApp.

    Parámetros:
        destinatario (str): Número de WhatsApp del destinatario.
        plantilla (str): Nombre de la plantilla aprobada.
        idioma (str): Código del idioma de la plantilla.

    Retorno:
        dict: Respuesta de la API de WhatsApp.
    """

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

    respuesta = requests.post(
        url,
        headers=encabezados,
        json=datos
    )

    return respuesta.json()