from conexion import Conexion
from persona import Persona

class PersonaDao:

    # ATRIBUTOS PRIVADOS (SQL)
    _SELECCIONAR = "SELECT * FROM persona"

    _INSERTAR = """
    INSERT INTO persona(nombre, apellido, email)
    VALUES(?,?,?)
    """

    _ACTUALIZAR = """
    UPDATE persona
    SET nombre=?, apellido=?, email=?
    WHERE id_persona=?
    """

    _ELIMINAR = """
    DELETE FROM persona
    WHERE id_persona=?
    """

    # CREAR TABLA
    @classmethod
    def crearTabla(cls):

        cursor = Conexion.obtenerCursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS persona(
            id_persona INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellido TEXT,
            email TEXT
        )
        """)

        Conexion.conexion.commit()

        Conexion.cerrar()

    # SELECT
    @classmethod
    def seleccionar(cls):

        cursor = Conexion.obtenerCursor()

        cursor.execute(cls._SELECCIONAR)

        registros = cursor.fetchall()

        personas = []

        for registro in registros:

            persona = Persona(
                registro[0],
                registro[1],
                registro[2],
                registro[3]
            )

            personas.append(persona)

        Conexion.cerrar()

        return personas

    # INSERT
    @classmethod
    def insertar(cls, persona):

        cursor = Conexion.obtenerCursor()

        valores = (
            persona.nombre,
            persona.apellido,
            persona.email
        )

        cursor.execute(cls._INSERTAR, valores)

        Conexion.conexion.commit()

        Conexion.cerrar()

    # UPDATE
    @classmethod
    def actualizar(cls, persona):

        cursor = Conexion.obtenerCursor()

        valores = (
            persona.nombre,
            persona.apellido,
            persona.email,
            persona.id_persona
        )

        cursor.execute(cls._ACTUALIZAR, valores)

        Conexion.conexion.commit()

        Conexion.cerrar()

    # DELETE
    @classmethod
    def eliminar(cls, persona):

        cursor = Conexion.obtenerCursor()

        valores = (persona.id_persona,)

        cursor.execute(cls._ELIMINAR, valores)

        Conexion.conexion.commit()

        Conexion.cerrar()
