
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")


def enviar_mensaje(destinatario, mensaje):
    """
    Envía un mensaje de prueba mediante WhatsApp Cloud API.

    Parámetros:
        destinatario (str): Número de WhatsApp que recibe el mensaje.
        mensaje (str): Texto del mensaje (no utilizado en esta prueba).

    Retorno:
        dict: Respuesta de la API de WhatsApp.
    """

    url = f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    datos = {
        "messaging_product": "whatsapp",
        "to": destinatario,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {
                "code": "en_US"
            }
        }
    }

    respuesta = requests.post(
        url,
        headers=headers,
        json=datos
    )

    print("Código de respuesta:", respuesta.status_code)
    print("Respuesta de WhatsApp:", respuesta.json())

    return respuesta.json()


if __name__ == "__main__":

    destinatario = input(
        "Ingresá el número de WhatsApp destinatario: "
    )

    mensaje = "¡Hola! Soy Calendi, tu asistente de calendario."

    resultado = enviar_mensaje(
        destinatario,
        mensaje
    )

    print(resultado)
