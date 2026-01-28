#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:40:04 2024

@author: fernd
"""
from Interfaz_Encolable import *
from Nodo import *
from typing import TypeVar

T = TypeVar('T')


class Cola(Encolable):

    def __init__(self):
        self.__inicio = None
        self.__final = None
        self.__tam = 0

    def encolar(self, elemento: T):
        """Agrega un nuevo elemento al final de la cola"""
        nuevo_nodo = Nodo(elemento)
        if self.esta_vacio():
            self.__inicio = self.__final = nuevo_nodo
        else:
            self.__final.siguiente = nuevo_nodo
            self.__final = nuevo_nodo
        self.__tam += 1

    def desencolar(self) -> T:
        """Elimina y devuelve el elemento del frente de la cola"""
        if not self.esta_vacio():
            valor = self.__inicio.elemento
            self.__inicio = self.__inicio.siguiente
            # Si se desencola el último elemento
            if self.__inicio is None:
                self.__final = None
            self.__tam -= 1
            return valor

    def tamanio(self) -> T:
        """Devuelve el tamaño de la cola"""
        return self.__tam

    def esta_vacio(self) -> bool:
        """Verifica si la cola está vacía"""
        return self.__inicio is None

    def vaciar(self):
        """Vacía la cola"""
        self.__inicio = self.__final = None
        self.__tam = 0

    # Métodos adicionales para la accesibilidad de la cola

    def contiene(self, elemento: T) -> bool:
        """
        Método que permite saber si un elemento se encuentra contenido dentro de la Cola.
        Este método no afecta el estado de la Cola.
        """
        return self.buscar(elemento) is not None

    def buscar(self, elemento: T) -> Nodo:
        """
        Método que busca el Nodo que contiene el elemento pasado como parámetro.
        Este método no afecta el estado de la Cola.
        """
        actual = self.__inicio
        while actual is not None:
            if actual.elemento == elemento:
                return actual
            actual = actual.siguiente
        return None

    def __str__(self) -> str:
        """Método que permite imprimir la Cola en formato cadena."""
        elementos = "Cola: "
        for elem in self:
            elementos += str(elem) + ", "
        return elementos.rstrip(", ")

    def __iter__(self):
        """Método que inicializa el iterador de la Cola."""
        self.pos = self.__inicio
        return self

    def __next__(self) -> T:
        """Método que permite obtener el siguiente elemento de la Cola."""
        if self.pos is not None:
            valor = self.pos.elemento
            self.pos = self.pos.siguiente
            return valor
        else:
            raise StopIteration
