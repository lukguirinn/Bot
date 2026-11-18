
"""
Gestiona las conexiones de usuarios de Calendi mediante SQLite.
"""

import os
import sqlite3
from pathlib import Path


RUTA_BASE = Path(__file__).resolve().parent.parent
DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    str(RUTA_BASE / "calendi.db")
)


def conectar_db():
    """
    Establece una conexión con SQLite.

    Retorno:
        sqlite3.Connection: Conexión a la base de datos.
    """

    return sqlite3.connect(DATABASE_PATH)


def inicializar_db():
    """
    Crea la tabla de conexiones de Google si no existe.
    """

    with conectar_db() as conexion:
        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS conexiones_google (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telefono TEXT UNIQUE NOT NULL,
                credenciales_cifradas TEXT NOT NULL,
                fecha_actualizacion TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


def guardar_conexion(telefono: str, credenciales: str):
    """
    Guarda o actualiza las credenciales cifradas de un usuario.

    Parámetros:
        telefono (str): Número de WhatsApp.
        credenciales (str): Credenciales cifradas.

    Retorno:
        None
    """

    with conectar_db() as conexion:
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO conexiones_google
            (telefono, credenciales_cifradas)
            VALUES (?, ?)
            ON CONFLICT(telefono)
            DO UPDATE SET
                credenciales_cifradas = excluded.credenciales_cifradas,
                fecha_actualizacion = CURRENT_TIMESTAMP
        """, (telefono, credenciales))


def obtener_conexion(telefono: str):
    """
    Busca las credenciales de un usuario.

    Parámetros:
        telefono (str): Número de WhatsApp.

    Retorno:
        str | None: Credenciales cifradas o None.
    """

    with conectar_db() as conexion:
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT credenciales_cifradas
            FROM conexiones_google
            WHERE telefono = ?
        """, (telefono,))

        resultado = cursor.fetchone()

    if resultado:
        return resultado[0]

    return None


def eliminar_conexion(telefono: str):
    """
    Elimina la conexión de Google de un usuario.

    Parámetros:
        telefono (str): Número de WhatsApp.

    Retorno:
        None
    """

    with conectar_db() as conexion:
        cursor = conexion.cursor()

        cursor.execute("""
            DELETE FROM conexiones_google
            WHERE telefono = ?
        """, (telefono,))
