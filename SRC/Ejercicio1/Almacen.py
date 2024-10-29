# Programa: Almacen.py
# Objetivo: Clase que modela una consola de videojuegos.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 28-10-2024

import Clase_Cola as cC
import Clase_Pila as cP


class Almacen:
    """
    Clase que modela el almacen del ejercicio 1.
    """
    def __init__(self):
        """
        Constructor del Almacen.
        Crea la banda magnetica vacia como una cola.
        Crea una pila de solicitudes como una pila vacia.
        """
        self.__banda_magnetica = cC.Cola()
        self.__solicitudes = cP.Pila()

    # Metodos Get
    @property
    def banda_magnetica(self):
        """
        Metodo GET para devolver banda magnetica.
        return: La banda magnetica
        :rtype: cC.Cola
        """
        return self.__banda_magnetica

    @property
    def solicitudes(self):
        """
        Metodo GET para devolver la pila de solicitudes.
        return: La pila de solicitudes
        :rtype: cP.Pila
        """
        return self.__solicitudes

    # Metodos set
    @banda_magnetica.setter
    def banda_magnetica(self, nueva_banda_magnetica):
        """
        Metodo que permite establecer una nueva banda magnetica
        :param nueva_banda_magnetica:
        """
        if isinstance(nueva_banda_magnetica, cC.Cola):
            self.__banda_magnetica = nueva_banda_magnetica
        else:
            raise TypeError

    @solicitudes.setter
    def solicitudes(self, solicitudes):
        """
        Metodo que permite establecer una nueva pila de solicitudes
        :param solicitudes:
        """
        if isinstance(solicitudes, cP.Pila):
            self.__solicitudes = solicitudes
        else:
            raise TypeError

    def __str__(self):
        """
        Metodo que permite imprimir la banda magnetica y la pila de solicitudes.
        :return: La banda magnetica y la pila de solicitudes
        :rtype: str
        """
        return ("\nBanda magnetica: \n" + self.__banda_magnetica.__str__() +
                "\nSolicitudes: \n" + self.__solicitudes.__str__())
