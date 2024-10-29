# Programa: Pila.py
# Objetivo: Clase abstracta que permite simular la interfaz para el TAD Pila.
#           Se implementa la "interfaz" Apilable
# Autor: Gerardo Avilés
# Version: 17-09-2024

import Nodo as n
import Interfaz_Apilable as p
from typing import TypeVar

T = TypeVar('T')


class Pila(p.Apilable):
    def __init__(self):
        """
        Constructor por omisión de la clase Pila
        """
        self.__top = None

    @property
    def top(self) -> n.Nodo:
        """
        Método GET para devolver el nodo top
        :return: El nodo inicio
        :rtype: n.Nodo
        """
        return self.__top

    def push(self, elemento: T):
        """
        Método que permite agregar un elemento en el tope de la Pila.
        Complejidad: O(1)
        :param elemento: El elemento que se va a almacenar en el Nodo
        """
        self.__top = n.Nodo(elemento, self.__top)

    def pop(self):
        """
        Método que permite eliminar el elemento que se encuentra en el
        tope de la Pila.
        Complejidad: O(1)
        :return: El elemento del tope de la Pila, None si la pila está vacía
        :rtype: T
        """
        if self.esta_vacia():
            return None
        dato = self.__top.elemento
        self.__top = self.__top.siguiente
        return dato

    def tope(self):
        """
        Método que devuelve el elemento que está en el tope de la Pila, sin
        eliminarlo.
        Complejidad: O(1).
        :return: El elemento del tope de la Pila, None si la pila esta vacía
        :rtype: T
        """
        if self.esta_vacia():
            return None
        dato = self.__top.elemento
        return dato

    def esta_vacia(self) -> bool:
        """
        Método que permite saber sí una Pila está vacía.
        Complejidad: O(1)
        :return: True sí está vacío, False en otro caso.
        :rtype: bool
        """
        return self.__top is None

    def vaciar(self):
        """
        Método que permite vaciar la Pila.
        Complejidad: O(1)
        """
        self.__top = None

    def contiene(self, elemento: T) -> bool:
        """
        Método que permite saber sí un elemento se encuentra contenido
        dentro de la Pila. Este método no afecta el estado de la Pila
        Complejidad: O(n).
        :param elemento: El elemento a buscar
        :return: True si lo encontró, False en otro caso
        :rtype: bool
        """
        return self.buscar(elemento) is not None

    def buscar(self, elemento: T) -> n.Nodo:
        """
        Método que busca el Nodo que contiene en el elemento pasado como
        parámetro. Este método no afecta el estado de la Pila
        Complejidad: O(n).
        :param elemento: El elemento a buscar
        :return: El Nodo que contiene el elemento, None en caso contrario
        :rtype: bool
        """
        pos = self.__top
        while pos is not None and not pos.elemento == elemento:
            pos = pos.siguiente
        return pos

    def __str__(self):
        """
        Método que permite imprimir una Pila en formato cadena
        :return: La Pila en formato cadena de caracter
        :rtype: str
        """
        # Utilizando el iterador
        it1 = iter(self)
        pila = "Pila: "
        try:
            while True:
                elem = next(it1)
                pila += str(elem) + ", "
        except StopIteration:
            pass
        return pila

    def __iter__(self):
        """
        Método que permite inicializar el iterador de la Pila
        :return: Un objeto iterable
        """
        self.pos = self.__top
        return self

    def __next__(self) -> T:
        """
        Método que permite obtener el siguiente elemento de la Pila
        :return: El siguiente elemento de la Lista
        :rtype: T
        """
        if self.pos is not None:
            a = self.pos.elemento
            self.pos = self.pos.siguiente
            return a
        else:
            raise StopIteration
