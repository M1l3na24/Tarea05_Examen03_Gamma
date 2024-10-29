# Programa: Apilable.py
# Objetivo: Clase abstracta que permite simular la interfaz para el TAD Lista
# Autor: Gerardo Avilés
# Version: 17-09-2024

from abc import abstractmethod, ABCMeta
from typing import TypeVar

T = TypeVar('T')


class Apilable(metaclass=ABCMeta):
    @abstractmethod
    def push(self, elemento: T):
        """
        Método que permite agregar un elemento en el tope de la Pila.
        Complejidad: O(1)
        :param elemento: El elemento que se va a almacenar en el Nodo
        """
        pass

    @abstractmethod
    def pop(self) -> T:
        """
        Método que permite eliminar el elemento que se encuentra en el
        tope de la Pila.
        Complejidad: O(1)
        :return: El elemento del tope de la Pila, None si la pila esta vacía
        :rtype: T
        """
        pass

    @abstractmethod
    def tope(self) -> T:
        """
        Método que devuelve el elemento que está en el tope de la Pila, sin
        eliminarlo.
        Complejidad: O(1).
        :return: El elemento del tope de la Pila, None si la pila esta vacía
        :rtype: T
        """
        pass

    @abstractmethod
    def esta_vacia(self) -> bool:
        """
        Método que permite saber sí una Pila está vacía.
        Complejidad: O(1)
        :return: True sí está vacío, False en otro caso.
        :rtype: bool
        """
        pass

    @abstractmethod
    def vaciar(self):
        """
        Método que permite vaciar la Pila.
        Complejidad: O(1)
        """
        pass
