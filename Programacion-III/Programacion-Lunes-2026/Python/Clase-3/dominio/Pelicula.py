class Pelicula:
    """
    Representa una película dentro del sistema de catálogo.

    Esta clase encapsula los datos básicos de una película, permitiendo
    gestionar su nombre de forma protegida.
    """

    def __init__(self, nombre: str):
        """
        Inicializador de la clase Pelicula.

        Args:
            nombre (str): El nombre o título de la película.
        """
        self._nombre = nombre

    def __str__(self) -> str:
        """
        Devuelve una representación amigable en formato cadena del objeto.

        Returns:
            str: Nombre de la película formateado.
        """
        return f'Pelicula: {self._nombre}'

    @property
    def nombre(self) -> str:
        """
        Getter para el atributo nombre.

        Returns:
            str: El nombre de la película.
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Setter para el atributo nombre. Permite modificar el título.

        Args:
            nombre (str): El nuevo nombre de la película.
        """
        self._nombre = nombre