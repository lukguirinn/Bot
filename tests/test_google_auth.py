
"""
Pruebas de desconexión individual de Google Calendar.
"""

import unittest
from types import SimpleNamespace
from unittest.mock import patch, Mock

from src.google_auth import desconectar_google


class TestDesconexionGoogle(unittest.TestCase):

    @patch("src.google_auth.eliminar_conexion")
    @patch("src.google_auth.requests.post")
    @patch("src.google_auth.obtener_credenciales")
    def test_desconexion_exitosa(
        self,
        mock_credenciales,
        mock_post,
        mock_eliminar
    ):
        """
        Comprueba una desconexión con revocación exitosa.
        """

        mock_credenciales.return_value = SimpleNamespace(
            refresh_token="token_ficticio",
            token="access_ficticio"
        )

        mock_post.return_value = Mock(status_code=200)

        resultado = desconectar_google("5491100000000")

        self.assertTrue(resultado["desconectado"])
        self.assertTrue(resultado["revocacion_google"])

        mock_eliminar.assert_called_once_with("5491100000000")

    @patch("src.google_auth.eliminar_conexion")
    @patch("src.google_auth.requests.post")
    @patch("src.google_auth.obtener_credenciales")
    def test_error_de_revocacion(
        self,
        mock_credenciales,
        mock_post,
        mock_eliminar
    ):
        """
        Comprueba que se elimine la conexión local
        aunque Google no confirme la revocación.
        """

        mock_credenciales.return_value = SimpleNamespace(
            refresh_token="token_ficticio",
            token="access_ficticio"
        )

        mock_post.return_value = Mock(status_code=400)

        resultado = desconectar_google("5491100000000")

        self.assertTrue(resultado["desconectado"])
        self.assertFalse(resultado["revocacion_google"])

        mock_eliminar.assert_called_once_with("5491100000000")

    @patch("src.google_auth.eliminar_conexion")
    @patch("src.google_auth.obtener_credenciales")
    def test_usuario_sin_conexion(
        self,
        mock_credenciales,
        mock_eliminar
    ):
        """
        Comprueba el comportamiento cuando el usuario
        ya no tiene credenciales guardadas.
        """

        mock_credenciales.return_value = None

        resultado = desconectar_google("5491100000000")

        self.assertTrue(resultado["desconectado"])

        mock_eliminar.assert_called_once_with("5491100000000")

    @patch("src.google_auth.eliminar_conexion")
    def test_numero_invalido(self, mock_eliminar):
        """
        Comprueba que no se acepte un número inválido.
        """

        resultado = desconectar_google("numero_invalido")

        self.assertFalse(resultado["desconectado"])

        mock_eliminar.assert_not_called()


if __name__ == "__main__":
    unittest.main()
