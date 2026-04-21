
from Pelicula import Pelicula
from catalogo_peliculas import CatalogoPeliculas


def mostrar_menu():
    """
    Muestra por pantalla las opciones disponibles del sistema.
    """
    print("\n--- MENÚ ---")
    print("1) Agregar película")
    print("2) Listar películas")
    print("3) Eliminar archivo de películas")
    print("4) Salir")


# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        """
        Opción 1:
        Solicita al usuario el nombre de una película,
        crea un objeto Pelicula y lo guarda en el catálogo.
        """
        nombre = input("Nombre de la película: ")
        pelicula = Pelicula(nombre)
        CatalogoPeliculas.agregar_pelicula(pelicula)

    elif opcion == "2":
        """
        Opción 2:
        Muestra todas las películas almacenadas en el archivo.
        """
        CatalogoPeliculas.listar_peliculas()

    elif opcion == "3":
        """
        Opción 3:
        Elimina el archivo donde se almacenan las películas.
        """
        CatalogoPeliculas.eliminar()

    elif opcion == "4":
        """
        Opción 4:
        Finaliza la ejecución del programa.
        """
        print("Saliendo...")
        break

    else:
        """
        Manejo de errores:
        Opción inválida ingresada por el usuario.
        """
        print("Opción inválida")