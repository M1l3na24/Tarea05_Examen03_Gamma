# Programa: Prueba_Almacen.py
# Objetivo: Interfaz del ejercicio 1
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 28-10-2024

import Almacen as A
import Solicitud as T
import Consola_Videojuegos as cV
import XboxSerieS as xS
import XboxSerieX as xX
import PlayStation5 as p5


def crear_consola() -> cV.Consolavideojuegos:
    """
    Metodo para solicitar los datos y crear una consola de videojuegos.
    :return: Un objeto consola
    """
    while True:
        codigo = int(input("Escribe el codigo: "))
        nombre = input("Escribe el nombre (XboxSeriesS, XboxSeriesX, PlayStation5): ")
        emp_fabricante = input("Escribe el fabricante: ")
        precio = int(input("Escribe precio: "))
        # Creamos la consola segun su nombre
        if nombre == 'XboxSeriesX':
            consola = xX.XboxSerieX(codigo, emp_fabricante, precio)
            print(f'{consola} almacenada correctamente. \n')
            return consola
        elif nombre == 'XboxSeriesS':
            consola = xS.XboxSerieS(codigo, emp_fabricante, precio)
            print(f'{consola} almacenada correctamente. \n')
            return consola
        elif nombre == 'PlayStation5':
            consola = p5.PlayStation5(codigo, emp_fabricante, precio)
            print(f'{consola} almacenada correctamente. \n')
            return consola
        else:
            raise ValueError('Los datos no son validos.')


def crear_solicitud() -> T.Solicitud:
    """
    Metodo para solicitar los datos y crear una solicitud (tienda).
    :return: Un objeto Libro
    """
    while True:
        # rfc: str, nombre_tienda: str, cantidad_solicitada: int, nombre_consola: str
        rfc = input("Escribe el RFC: ")
        nombre_tienda = input("Escribe el nombre de la tienda: ")
        cantidad_solicitada = int(input("Escribe la catidad solicitada: "))
        nombre_consola = input("Escribe el nombre de la consola (XboxSeriesS, XboxSeriesX, PlayStation5): ")
        if nombre_tienda in ['XboxSeriesS', 'XboxSeriesX', 'PlayStation5']:
            # Creamos tienda
            tienda = T.Solicitud(rfc, nombre_tienda, cantidad_solicitada, nombre_consola)
            if isinstance(rfc, str) and isinstance(nombre_tienda, str) and isinstance(cantidad_solicitada, int):
                return tienda
        else:
            print("No son datos validos")


def menu_consultar_existencias() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar para consultar
    la existencia de alguna consola
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input("Como deseas consultar existencia:\n"
                        "1. Por codigo de producto\n"
                        "2. Por nombre de la consola\n"
                        "3. Por empresa fabricante.\n"
                        "S. Salir \n").upper()
        if opcionn not in "1,2,3,S" or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn


almacen = None

# Aqui comienza la interfaz
while True:

    print("1. Crear mi almacen (Se cargara toda la informacion existente)")
    print("2. Consulta el numero de existencias de alguna consola")
    print("3. Almacenar una nueva consola de videojuegos")
    print("4. Registrar una nueva solicitud de compra")
    print("[S]alir")
    accion = input("¿Que deseas hacer?: ").upper()
    if accion not in "1,2,3,4,S":
        print("No se que deseas hacer!\n")
        continue
    match accion:
        case "1":  # Crear mi almacen
            almacen = A.Almacen()
            almacen.leer_archivo_consolas('consolas.csv')
            almacen.leer_archivo_consolas('tiendas.csv')
            print("Se ha creado el almacen con los datos previos. \n")

        case "2":  # Consulta el numero de existencias de alguna consola
            if almacen is None:
                print("Debes crear primero un almacen!\n")
                continue
            else:
                respuesta = menu_consultar_existencias()
                existencias = 0
                if respuesta == '1':
                    codigo = input('Ingresa el codigo a consultar:')
                    existencias = almacen.consulta_existencias(codigo=int(codigo))
                elif respuesta == '2':
                    nombre = input('Ingresa el nombre a consultar (XboxSeriesS, XboxSeriesX, PlayStation5):')
                    if nombre not in ['XboxSeriesS', 'XboxSeriesX', 'PlayStation5']:
                        print('El nombre no es valido \n')
                        continue
                    existencias = almacen.consulta_existencias(nombre=nombre)
                elif respuesta == '3':
                    empresa = input('Ingresa la empresa a consultar:')
                    existencias = almacen.consulta_existencias(empresa_fabricante=empresa)
                print(f'Hay {existencias} consolas de ese tipo en existencia')

        case "3":  # Almacenar una nueva consola de videojuegos
            if almacen is None:
                print("Debes crear primero un almacen!\n")
                continue
            else:
                try:
                    consola = crear_consola()
                    almacen.banda_magnetica.encolar(consola)
                except ValueError:
                    print('Los datos ingresados no son validos \n')
                    continue

        case "4":   # Registrar una nueva solicitud de compra
            if almacen is None:
                print("Deber crear primero un almacen\n")
            else:
                soli = crear_solicitud()
                almacen.registrar_solicitud(soli)

        case "S":  # Salir
            almacen.escritura_consolas()
            almacen.escritura_solicitudes()
            print("La informacion del almacen se ha actualizado.\n")
            print("Hasta luego! :D\n")
            break
