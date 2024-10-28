# Programa: PlayStation5.py
# Objetivo: Clase que modela una consola de videojuegos del tipo PlayStation5.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 28-10-2024

import Consola_Videojuegos as cV


class PlayStation5(cV.Consolavideojuegos):
    """
    Clase de un objeto del tipo Play Station 5 que hereda de una consola
    de videojuegos.
    """
    def __init__(self, codigo: int, emp_fabricante: str, precio: int, nombre='Play Station 5'):
        """
        Constructor de un objeto Consola de videojuegos del tipo PlayStation5
                :param codigo - codigo de la PlayStation5
                :param nombre -  nombre de la PlayStation5
                :param emp_fabricante - la empresa que fabrico la PlayStation5
                :param precio - precio de la PlayStation5
        """
        super().__init__(codigo, nombre, emp_fabricante, precio)
