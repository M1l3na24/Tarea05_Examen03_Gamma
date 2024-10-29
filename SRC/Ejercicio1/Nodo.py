# Programa: Nodo.py
# Objetivo: Clase que implementa un Nodo como un elemento de una Lista Ligada
# Autor: Gerardo Avilés
# Version: 04-09-2024

class Nodo:
    def __init__(self, *params):
        """
        Constructor para los Nodos de la Lista Ligada
        :param params: Si se manda un parámetro, es el dato a guardar en la Lista,
                       el siguiente se inicia en None. Si se mandan dos parámetros,
                       el primero es el dato y el siguiente se apunta al otro Nodo
        """
        if len(params) == 1:
            self.elemento = params[0]
            self.siguiente = None
        elif len(params) == 2:
            self.elemento = params[0]
            self.siguiente = params[1]
