from persona import Persona
from personaDao import PersonaDao

# Creamos la tabla
PersonaDao.crearTabla()

# Creamos a la persona
persona1 = Persona(
    nombre="Candelaria",
    apellido="Ribotta",
    email="canderibotta@gmail.com"
)

PersonaDao.insertar(persona1)

# Mostrar personas
personas = PersonaDao.seleccionar()

for persona in personas:
    print(persona)
