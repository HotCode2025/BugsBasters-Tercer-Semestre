from capa_datos_persona.Persona import Persona
from capa_datos_persona.conexion import Conexion
from logger_base import log

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

    # Definimos los métodos de clase
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.getchall()
            personas = [] #creamos una lista
            for registro in registros:
                persona = Persona(registro[0]), registro[1], registro[2], registro[3]
                personas.append(persona)
                return personas



    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (
                persona.nombre,
                persona.apellido,
                persona.email
            )
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Persona insertada: {persona}")

    
    @classmethod
    def actualizar(cls, persona):
            with CursorDelPool() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f"Persona actualizada: {persona}")
                return cursor.rowcount


    @classmethod
    def eliminar(cls, persona):
            with CursorDelPool() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f"Los objetos eliminados son: {persona}")
                return cursor.rowcount
            

if __name__ == '__main__':
     # Eliminar un registro
     persona1 = Persona(id_persona=18)
     personas_eliminadas = PersonaDAO.eliminar(persona1)
     log.debug(f"Personas eliminadas. {personas_eliminadas}")

    # Actualizar un registro
    persona1 = Persona(1, "Juan", "Pena", "jpena@gmail.com")
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f"Personas actualizadas: {personas_actualizadas}")

     # Insertar un registro
     persona1 = Persona(nobre="Mateo", apellido="Torres", email="tejadam<cqgmail.com")
     personas_insertadas = PersonaDAO.insertar(persona1)
     log.debug(f"Personas insertadas: {personas_insertadas}")

    # Seleccionar objetos
     personas = PersonaDao.seleccionar()
     for persona in personas:
          log.debug(persona)

        
