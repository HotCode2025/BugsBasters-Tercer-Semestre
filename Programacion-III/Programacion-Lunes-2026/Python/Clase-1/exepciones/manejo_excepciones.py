"""
Programa principal para la demostración del manejo de excepciones en Python.
Permite realizar una división entre dos números capturando posibles errores 
como división por cero, tipos incorrectos, o la introducción de números iguales.
"""

from NumerosIgualesException import NumerosIgualesException

# Variable para almacenar el resultado de la operación
resultado = None

try:
    # Solicitamos la entrada del usuario y la convertimos a entero
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    
    # Verificamos si los números son iguales para lanzar la excepción personalizada
    if a == b:
        raise NumerosIgualesException('Son números iguales')
    
    # Realizamos la operación de división si no saltó ninguna excepción previa
    resultado = a / b
    
except TypeError as e:
    # Captura errores en caso de que ocurra un problema con los tipos de datos (aunque 'int()' lanza ValueError en caso de error)
    print(f'TypeError - Ocurrió un error: {type(e)}')
    
except ZeroDivisionError as e:
    # Captura el error en caso de que el divisor (b) sea cero
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
    
except Exception as e:
    # Captura cualquier otra excepción genérica no prevista
    print(f'Exception - Ocurrió un error: {type(e)}')
    
else:
    # Bloque que se ejecuta únicamente si NO surgió ninguna excepción
    print("No se arrojo ninguna excepción")
    
finally: 
    # Bloque que SIEMPRE se ejecuta, sin importar si hubo o no excepciones.
    # Útil para liberar recursos o cerrar conexiones.
    print("Ejecución de este bloque finally")

# Imprimimos el resultado de la división y un mensaje de finalización
print(f'El resultado es: {resultado}')
print('Seguimos...')