# Programa: Tienda.py
# Objetivo: Clase que modela una tienda.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 28-10-2024


class Tienda:
    """
    Clase que modela un objeto Tienda, que podra hacer un pedido.
    """
    def __init__(self, rfc: str, nombre_tienda: str, cantidad_solicitada: int, nombre_consola: str):
        """
        Constructor del objeto tienda que tiene
        RFC, nombre, la cantidad solicitada de consolas de videojuegos y el nombre de la consola.
        :param rfc - RFC de latienda
        :param nombre_tienda -  nombre de la tienda
        :param cantidad_solicitada - la cantidad solicitada de consolas de videojuegos
        :param nombre_consola - el nombre de la consola
        """
        self.__rfc = rfc
        self.__nombre_tienda = nombre_tienda
        self.__cantidad_solicitada = cantidad_solicitada
        self.__nombre_consola = nombre_consola

    # Metodos GET
    @property
    def rfc(self):
        """
        Metodo para obtener el RFC de la tienda
        :return: El RFC de la tienda
        :rtype: str
        """
        return self.__rfc

    @property
    def nombre_tienda(self):
        """
        Metodo para obtener el nombre de la tiendd
        :return: El nombre de la tienda
        :rtype: str
        """
        return self.__nombre_tienda

    @property
    def cantidad_solicitada(self):
        """
        Metodo para obtener la cantidad solicitada de consolas por parte
        de la tienda.
        :return:La cantidad de consolas solicitadas
        :rtype: int
        """
        return self.__cantidad_solicitada

    @property
    def nombre_consola(self):
        """
        Metodo para obtener el nombre de la consola de videojuegos solicitada
        :return: El nombre de la consola de videojuegos solicitada
        :rtype: str
        """
        return self.__nombre_consola

    # Metodos SET
    @rfc.setter
    def rfc(self, rfc: int):
        """
        Metodo para modificar el RFC de la tienda
        :param rfc: El RFC de la tienda
        """
        self.__rfc = rfc

    @nombre_tienda.setter
    def nombre_tienda(self, nombre_tienda: int):
        """
        Metodo para modificar el nombre de la tienda
        :param nombre_tienda: El precio de la consola de videojuegos
        """
        self.__nombre_tienda = nombre_tienda

    @cantidad_solicitada.setter
    def cantidad_solicitada(self, cantidad_solicitada: int):
        """
        Metodo para modificar la cantidad solicitada de consolas
        :param cantidad_solicitada: La cantidad solicitada de consolas de videojuegos
        """
        self.__cantidad_solicitada = cantidad_solicitada

    @nombre_consola.setter
    def nombre_consola(self, nombre_consola: str):
        """
        Metodo para modificar elnombre de la consola de videojuegos solicitada
        :param nombre_consola: El nombre de la consola de videojuegos solicitada
        """
        self.__nombre_consola = nombre_consola

    def __iter__(self):
        """
        Metodo que devuelve una representacion iterable de la tienda
        :return: La representacion en formato iterable de la tienda
        :rtype: iterable
        """
        return iter([self.__rfc, self.__nombre_tienda, self.__cantidad_solicitada, self.__nombre_consola])

    def __str__(self):
        """
        Metodo que permite definir una tienda en formato cadena
        :return: La tienda en formato str
        :rtype: str
        """
        return ("RFC: {} | Tienda: {} | "
                "Cantidad solicitada: {} | Tipo: {}").format(self.__rfc, self.__nombre_tienda,
                                                             self.__cantidad_solicitada, self.__nombre_consola)
