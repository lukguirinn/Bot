"""
Contiene la lógica principal de procesamiento de mensajes de Calendi.
"""


def procesar_mensaje(mensaje, remitente):
    """
    Procesa el mensaje recibido por WhatsApp.

    Parámetros:
        mensaje (str): Texto recibido del usuario.
        remitente (str): Número de WhatsApp del usuario.

    Retorno:
        str: Identificador de la respuesta correspondiente.
    """

    mensaje = mensaje.lower().strip()

    if mensaje == "hola":
        return "saludo"

    elif mensaje == "ayuda":
        return "ayuda"

    else:
        return "desconocido"