# Programa: Consola_Videojuegos.py
# Objetivo: Clase que modela una consola de videojuegos.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 28-10-2024


class Consolavideojuegos:
    """
    Clase que modela un objeto consola de videojuegos
    """
    def __init__(self, codigo: int, nombre: str, emp_fabricante: str, precio: int):
        """
        Constructor del objeto Consola de videojuegos que tiene
        codigo, nombre, empresa fabricante y precio.
        :param codigo - codigo de la consola de videojuegos
        :param nombre -  nombre de la consola de videojuegos
        :param emp_fabricante - la empresa que fabrico la consola de videojuegos
        :param precio - precio de la consola de videojuegos
        """
        self.__codigo = codigo
        self.__nombre = nombre
        self.__fabricante = emp_fabricante
        self.__precio = precio

    # Metodos GET
    @property
    def codigo(self):
        """
        Metodo para obtener el codigo de la consola de videojuegos
        :return: El codigo de la consola de videojuegos
        :rtype: int
        """
        return self.__codigo

    @property
    def nombre(self):
        """
        Metodo para obtener el nombre de la consola de videojuegos
        :return: El nombre de la consola de videojuegos
        :rtype: str
        """
        return self.__nombre

    @property
    def fabricante(self):
        """
        Metodo para obtener la empresa fabricante de la consola de videojuegos
        :return:La empresa fabricante de la consola de videojuegos
        :rtype: str
        """
        return self.__fabricante

    @property
    def precio(self):
        """
        Metodo para obtener el precio de la consola de videojuegos
        :return: El precio de la consola de videojuegos
        :rtype: int
        """
        return self.__precio

    # Metodos SET
    @codigo.setter
    def codigo(self, codigo: int):
        """
        Metodo para modificar el codigo de la consola de videojuegos
        :param codigo: El codigo de la consola de videojuegos
        """
        self.__codigo = codigo

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Metodo para modificar el nombre de la consola de videojuegos
        :param nombre: El nombre de la consola de videojuegos
        """
        self.__nombre = nombre

    @fabricante.setter
    def fabricante(self, fabricante: str):
        """
        Metodo para modificar el fabricante de la consola de videojuegos
        :param fabricante: El fabricante de la consola de videojuegos
        """
        self.__fabricante = fabricante

    @precio.setter
    def precio(self, precio: int):
        """
        Metodo para modificar el precio de la consola de videojuegos
        :param precio: El precio de la consola de videojuegos
        """
        self.__precio = precio

    def __iter__(self):
        """
        Metodo que devuelve una representacion iterable de la consola de videojuegos
        :return: La representacion en formato iterable de la consola de videojuegos
        :rtype: iterable
        """
        return iter([self.__codigo, self.__nombre, self.__fabricante, self.__precio])

    def __str__(self):
        """
        Metodo que permite definir una consola de videojuegos en formato cadena
        :return: La consola de videojuegos en formato str
        :rtype: str
        """
        return ("Consola: {} | Nombre: {} | "
                "Empresa Fabricante: {} | Precio: {}").format(self.__codigo, self.__nombre, self.__fabricante,
                                                              self.__precio)
