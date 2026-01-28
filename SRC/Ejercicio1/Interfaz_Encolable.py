# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 07:01:42 2023

@author: HP
"""
from abc import ABC, abstractmethod
from typing import TypeVar

# Definimos un tipo genérico T
T = TypeVar('T')


class Encolable(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def encolar(self, elemento: T):
        """Agrega un elemento a la cola."""
        pass

    @abstractmethod
    def desencolar(self) -> T:
        """Remueve y devuelve el elemento al frente de la cola."""
        pass

    @abstractmethod
    def tamanio(self) -> int:
        """Devuelve el tamaño de la cola"""
        pass

    @abstractmethod
    def esta_vacio(self) -> bool:
        """Devuelve True si la cola está vacía, de lo contrario False."""
        pass

    @abstractmethod
    def vaciar(self):
        """Permite vaciar la cola."""
        pass
