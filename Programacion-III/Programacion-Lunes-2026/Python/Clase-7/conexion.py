import sqlite3

class Conexion:

    DATABASE = "personas.db"

    conexion = None
    cursor = None

    @classmethod
    def obtenerConexion(cls):

        cls.conexion = sqlite3.connect(cls.DATABASE)

        return cls.conexion

    @classmethod
    def obtenerCursor(cls):

        cls.cursor = cls.obtenerConexion().cursor()

        return cls.cursor

    @classmethod
    def cerrar(cls):

        if cls.cursor:
            cls.cursor.close()

        if cls.conexion:
            cls.conexion.close()
