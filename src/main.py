"""
Punto de entrada principal de Calendi.
Inicia el servidor Flask.
"""

from src.webhook import app
from src.whatsapp import verificar_token

verificar_token()

if __name__ == "__main__":
    app.run(port=5000, debug=True)