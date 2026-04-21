import os

class CatalogoPeliculas:
    """
    Clase de capa de servicio para gestionar el catálogo de películas.
    
    Esta clase maneja la persistencia de datos en un archivo de texto plano.
    Todos sus métodos son de clase (estáticos) para facilitar el acceso sin
    necesidad de instanciar el servicio.
    """
    
    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
        """
        Añade una nueva película al archivo de texto.
        
        Args:
            pelicula (Pelicula): Instancia del objeto Pelicula a guardar.
        """
        try:
            with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
                archivo.write(f'{pelicula.nombre}\n')
        except Exception as e:
            print(f'Error al agregar película: {e}')

    @classmethod
    def listar_peliculas(cls):
        """
        Lee y muestra en consola el contenido del catálogo.
        
        Nota:
            Utiliza el modo de lectura 'r' y maneja la visualización formateada.
        """
        try:
            with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
                print(' Catálogo de Películas '.center(50, '-'))
                print(archivo.read())
        except FileNotFoundError:
            print('El archivo de catálogo no existe. Agrega una película primero.')
        except Exception as e:
            print(f'Error al listar películas: {e}')

    @classmethod
    def eliminar_peliculas(cls):
        """
        Elimina físicamente el archivo del catálogo del sistema de archivos.
        """
        try:
            if os.path.exists(cls.ruta_archivo):
                os.remove(cls.ruta_archivo)
                print(f'Archivo eliminado con éxito: {cls.ruta_archivo}')
            else:
                print('No existe un archivo para eliminar.')
        except Exception as e:
            print(f'Error al intentar eliminar el archivo: {e}')