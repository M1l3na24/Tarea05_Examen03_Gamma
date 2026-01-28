# Programa: Almacen.py
# Objetivo: Clase que modela un objeto del tipo Almacen.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 29-10-2024

import Clase_Cola as cC
import Clase_Pila as cP
import csv
import XboxSerieS as xS
import XboxSerieX as xX
import PlayStation5 as pS
import Solicitud as So


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

    # Metodos extra para el ejercicio
    def leer_archivo_consolas(self, archivo: str):
        """
        Metodo para leer un archivo y construir una banda magnetica.
        :param archivo: El nombre del archivo que se va a leer
        :return: Una Cola (Banda magnetica)
        """
        existe = False  # El archivo no existe
        while not existe:
            try:
                with open(archivo, encoding="UTF8", newline="") as file:
                    lector = csv.reader(file)
                    lector.__next__()  # Salta la primera linea
                    for fila in lector:
                        if fila[1] == "XboxSeriesX":
                            self.banda_magnetica.encolar(xX.XboxSerieX(int(fila[0]),  # codigo
                                                                       fila[2],  # emp_fabricante
                                                                       int(fila[3])))  # precio
                        elif fila[1] == "XboxSeriesS":
                            self.banda_magnetica.encolar(xS.XboxSerieS(int(fila[0]),  # codigo
                                                                       fila[2],  # emp_fabricante
                                                                       int(fila[3])))  # precio
                        elif fila[1] == "PlayStation5":
                            self.banda_magnetica.encolar(pS.PlayStation5(int(fila[0]),  # codigo
                                                                         fila[2],  # emp_fabricante
                                                                         int(fila[3])))  # precio
                    existe = True
                    print(f"El archivo {archivo} se leyo exitosamente!\n")
            except FileNotFoundError:
                print("El archivo no existe!\n")
                archivo = input("Escribe el nombre del archivo CSV: ")
            except OSError:
                print("No es una entrada valida\n")
                break

    def leer_archivo_tiendas(self, archivo: str):
        """
        Metodo para leer un archivo y construir una pila de solicitudes.
        :param archivo: El nombre del archivo que se va a leer
        :return: Una Pila (solicitudes)
        """
        existe = False  # El archivo no existe
        while not existe:
            try:
                with open(archivo, encoding="UTF8", newline="") as file:
                    lector = csv.reader(file)
                    lector.__next__()  # Salta la primera linea
                    for fila in lector:
                        self.solicitudes.push(So.Solicitud(fila[0],  # rfc
                                              fila[1],  # nombre_tienda
                                              int(fila[2]),  # cantidad_solicitada
                                              fila[3]))  # nombre_consola
                    existe = True
                    print(f"El archivo {archivo} se leyo exitosamente!\n")
            except FileNotFoundError:
                print("El archivo no existe!\n")
                archivo = input("Escribe el nombre del archivo CSV: ")
            except OSError:
                print("No es una entrada valida\n")
                break

    def escritura_consolas(self):
        """
        Metodo que guarda la informacion de las consolas existentes en un archivo csv,
        para ello se utilizara los iteradores de la Cola.
        """
        nombre = 'consolas.csv'
        f = open(nombre, 'w')
        encabezado = 'codigo,nombre,emp_fabricante,precio\n'
        f.write(encabezado)
        for consola in self.banda_magnetica:
            if consola is not None:
                cadena = ''
                for atributo in consola:
                    cadena += str(atributo) + ','
                cadena = cadena[:-1] + '\n'
                f.write(cadena)
        f.close()
        print(f'Se ha guardado la informacion en el archivo "{nombre}"\n')

    def escritura_solicitudes(self):
        """
        Metodo que guarda la informacion de las nuevas solicitudes en un archivo csv,
        agregando los datos sin borrar la informacion existente.
        """
        nombre = 'tiendas.csv'
        # modo 'a' (append) para agregar informacion sin borrar el contenido existente
        with open(nombre, 'a') as f:
            # Verificar si el archivo esta vacio
            if f.tell() == 0:
                encabezado = 'rfc,nombre_tienda,cantidad_solicitada,nombre_consola\n'
                f.write(encabezado)

            # Iteramos sobre las solicitudes para escribir cada una en una linea
            for solicitud in self.solicitudes:
                if solicitud is not None:
                    cadena = ''
                    for atributo in solicitud:
                        cadena += str(atributo) + ','
                    cadena = cadena[:-1]   # Eliminamos la ultima coma y aniadimos salto de linea

                    # Agregamos un salto de línea al inicio si no es la primera solicitud escrita
                    if f.tell() > 0:  # Si no estamos al inicio, aniadir una nueva línea antes
                        cadena = '\n' + cadena

                    f.write(cadena)  # Escribir la solicitud

        print(f'Se ha guardado la nueva informacion en el archivo "{nombre}"\n')

    def consulta_existencias(self, codigo=None, nombre=None, empresa_fabricante=None):
        """
        Metodo para consultar la existencia de cierto tipo de consola dependiendo del
        parametro.
        :param codigo: Consultar por codigo de consola
        :param nombre: Consultar por nombre de consola
        :param empresa_fabricante: Consultar por fabricante de consola
        :return:
        """
        aux = 0
        for consola in self.banda_magnetica:
            if ((codigo and consola.codigo == codigo) or (nombre and consola.nombre == nombre) or (
                    empresa_fabricante and consola.fabricante == empresa_fabricante)):
                aux += 1
        print(f"Existencias encontradas: {aux}")
        return aux

    def registrar_solicitud(self, solicitud):
        """
        Metodo para registrar un nueva solicitud y simular la venta de consolas.
        :param solicitud: Objeto del tipo Solicitud
        """
        # Verificar existencias en la cola
        existencias = self.consulta_existencias(nombre=solicitud.nombre_consola)
        if existencias >= solicitud.cantidad_solicitada:  # tengo suficientes
            # Proceso de venta
            precio_total = 0  # NOTA: En esta simulacion las consolas varian en precio aunque sean del mismo tipo
            contador = 0
            cola_auxiliar = cC.Cola()
            while contador < solicitud.cantidad_solicitada:
                # Retirar consolas de la cola
                consola_a = self.banda_magnetica.desencolar()
                if consola_a.nombre == solicitud.nombre_consola:
                    precio_total += consola_a.precio
                    contador += 1
                else:
                    cola_auxiliar.encolar(consola_a)
            # salgo del while cuando ya complete el pedido
            if not self.banda_magnetica.esta_vacio():
                for i in range(self.banda_magnetica.tamanio()):
                    a = self.banda_magnetica.desencolar()
                    cola_auxiliar.encolar(a)

                for i in range(cola_auxiliar.tamanio()):
                    b = cola_auxiliar.desencolar()
                    self.banda_magnetica.encolar(b)

            else:  # en caso de que me tomo vaciar la banda magnetica
                #  significa que ya tengo todos en la cola auxiliar
                for i in range(cola_auxiliar.tamanio()):
                    b = cola_auxiliar.desencolar()
                    self.banda_magnetica.encolar(b)

            print(f"Venta realizada para {solicitud.nombre_tienda}:")
            print(f"RFC {solicitud.rfc}")
            print(f"Consola: {solicitud.nombre_consola}, Cantidad: {solicitud.cantidad_solicitada}, "
                  f"Total a pagar: $ {precio_total}")

            # Apilar solicitud solo si hay existencias
            self.solicitudes.push(solicitud)
        else:
            print("No hay suficientes existencias para completar la solicitud.\n")
