
"""
Herramienta para verificar el token y los permisos de WhatsApp.
"""

import requests
from src.whatsapp import TOKEN, PHONE_NUMBER_ID


def verificar_token():
    """
    Verifica el token, sus permisos y el acceso al número de WhatsApp.
    """

    encabezados = {
        "Authorization": f"Bearer {TOKEN}"
    }

    respuesta = requests.get(
        "https://graph.facebook.com/v23.0/me",
        headers=encabezados,
        timeout=20
    )

    print("VERIFICACION TOKEN:", respuesta.status_code)
    print("DATOS CUENTA:", respuesta.json())

    permisos = requests.get(
        "https://graph.facebook.com/v23.0/me/permissions",
        headers=encabezados,
        timeout=20
    )

    print("PERMISOS:", permisos.json())

    numero = requests.get(
        f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}",
        headers=encabezados,
        timeout=20
    )

    print("PHONE NUMBER ID:", numero.status_code)
    print("DATOS DEL NUMERO:", numero.json())


if __name__ == "__main__":
    verificar_token()
