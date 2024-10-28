# Programa: XboxSerieX.py
# Objetivo: Clase que modela una consola de videojuegos del tipo XboxSerieX.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 28-10-2024

import Consola_Videojuegos as cV


class XboxSerieX(cV.Consolavideojuegos):
    """
    Clase de un objeto del tipo Xbox Series X que hereda de una consola
    de videojuegos.
    """
    def __init__(self, codigo: int, emp_fabricante: str, precio: int, nombre='Xbox Series X'):
        """
        Constructor de un objeto Consola de videojuegos del tipo XboxSerieX
                :param codigo - codigo del XboxSerieX
                :param nombre -  nombre del XboxSerieX
                :param emp_fabricante - la empresa que fabrico el XboxSerieX
                :param precio - precio del XboxSerieX
        """
        super().__init__(codigo, nombre, emp_fabricante, precio)
