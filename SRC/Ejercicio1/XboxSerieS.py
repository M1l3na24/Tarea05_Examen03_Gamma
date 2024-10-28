# Programa: XboxSerieS.py
# Objetivo: Clase que modela una consola de videojuegos del tipo XboxSerieS.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 28-10-2024

import Consola_Videojuegos as cV


class XboxSerieS(cV.Consolavideojuegos):
    """
    Clase de un objeto del tipo Xbox Series S que hereda de una consola
    de videojuegos.
    """
    def __init__(self, codigo: int, emp_fabricante: str, precio: int, nombre='Xbox Series S'):
        """
        Constructor de un objeto Consola de videojuegos del tipo XboxSerieS
                :param codigo - codigo del XboxSerieS
                :param nombre -  nombre del XboxSerieS
                :param emp_fabricante - la empresa que fabrico el XboxSerieS
                :param precio - precio del XboxSerieS
        """
        super().__init__(codigo, nombre, emp_fabricante, precio)
