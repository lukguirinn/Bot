from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "calendi_webhook_2026"


@app.route("/webhook", methods=["GET"])
def verificar_webhook():
    """
    Verifica la conexión del webhook con Meta.

    Retorno:
        str: El desafío enviado por Meta si la verificación es válida.
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
    Recibe notificaciones de WhatsApp enviadas por Meta.

    Retorno:
        str: Confirmación de recepción.
    """

    datos = request.get_json()

    print("Notificación recibida:")
    print(datos)

    return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)