from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas as cp

"""
Módulo de interfaz de usuario para el Catálogo de Películas.

Este script ejecuta un menú interactivo por consola que permite al usuario
realizar operaciones CRUD básicas sobre el catálogo de películas utilizando
la clase CatalogoPeliculas.
"""

opcion = None

while opcion != 4:
    try:
        print('\nMENU DE OPCIONES')
        print('1. Agregar Película')
        print('2. Listar Películas')
        print('3. Eliminar catálogo de películas')
        print('4. Salir')
        
        opcion = int(input('Seleccione una opción (1-4): '))

        if opcion == 1:
            # Captura de datos para crear el objeto de dominio
            nombre_pelicula = input('Ingrese el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
            print('Película agregada correctamente.')
            
        elif opcion == 2:
            # Llamada al servicio de listado
            cp.listar_peliculas()
            
        elif opcion == 3:
            # Llamada al servicio de eliminación de archivo
            cp.eliminar_peliculas()
            
    except ValueError:
        print('Error: Por favor, ingrese un número entero válido.')
        opcion = None
    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')
        opcion = None

print('Finalizando programa. ¡Hasta pronto!')