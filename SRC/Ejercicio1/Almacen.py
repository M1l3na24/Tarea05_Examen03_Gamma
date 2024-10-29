# Programa: Almacen.py
# Objetivo: Clase que modela una consola de videojuegos.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 28-10-2024

import Clase_Cola as cC
import Clase_Pila as cP
import csv
import XboxSerieS as xS
import XboxSerieX as xX
import PlayStation5 as p5
import Solicitud as s


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

    def leer_archivo_consolas(self, archivo: str):
        """
        Metodo para leer un archivo y construir banda magnetica.
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
                            self.banda_magnetica.encolar(p5.PlayStation5(int(fila[0]),  # codigo
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
                        self.solicitudes.push(s.Solicitud(fila[0],  # rfc
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
        Metodo que guarda la informacion de las solicitudes existentes en un archivo csv,
        para ello se utilizara los iteradores de la Cola.
        """
        nombre = 'tiendas.csv'
        f = open(nombre, 'w')
        encabezado = 'rfc,nombre_tienda,cantidad_solicitada,nombre_consola\n'
        f.write(encabezado)
        for solicitud in self.solicitudes:
            if solicitud is not None:
                cadena = ''
                for atributo in solicitud:
                    cadena += str(atributo) + ','
                cadena = cadena[:-1] + '\n'
                f.write(cadena)
        f.close()
        print(f'Se ha guardado la informacion en el archivo "{nombre}"\n')

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
                    empresa_fabricante and consola.empresa_fabricante == empresa_fabricante)):
                aux += 1
        print(f"Existencias encontradas: {aux}")
        return aux

    def registrar_solicitud(self, solicitud):
        # Verificar existencias en la cola
        existencias = self.consulta_existencias(nombre=solicitud.nombre_consola)
        if existencias >= solicitud.cantidad_solicitada:
            # Proceso de venta
            precio_total = 0
            # Retirar consolas de la cola
            for _ in range(solicitud.cantidad_solicitada):
                a = self.banda_magnetica.desencolar()
                precio_total += a.precio

            print(f"Venta realizada para {solicitud.nombre_tienda}:")
            print(f"Consola: {solicitud.nombre_consola}, Cantidad: {solicitud.cantidad_solicitada}, "
                  f"Total a pagar: {precio_total}")

            # Apilar solicitud solo si hay existencias
            self.solicitudes.push(solicitud)
        else:
            print("No hay suficientes existencias para completar la solicitud.")
