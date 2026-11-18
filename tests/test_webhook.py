
"""
Pruebas de integración del webhook de WhatsApp.
"""

import unittest
from unittest.mock import patch

from src.webhook import app


class TestWebhook(unittest.TestCase):

    def setUp(self):
        """
        Configura el cliente de pruebas de Flask.
        """

        app.config["TESTING"] = True
        self.cliente = app.test_client()

    @patch("src.webhook.desconectar_google")
    def test_solicitud_desconexion(self, mock_desconexion):
        """
        Comprueba que el webhook identifique la solicitud
        y utilice el número correcto del remitente.
        """

        mock_desconexion.return_value = {
            "desconectado": True,
            "revocacion_google": True
        }

        datos = {
            "entry": [
                {
                    "changes": [
                        {
                            "value": {
                                "messages": [
                                    {
                                        "from": "5491100000000",
                                        "type": "text",
                                        "text": {
                                            "body": "Desconectar Google"
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }

        respuesta = self.cliente.post(
            "/webhook",
            json=datos
        )

        self.assertEqual(respuesta.status_code, 200)

        mock_desconexion.assert_called_once_with(
            "5491100000000"
        )


if __name__ == "__main__":
    unittest.main()
