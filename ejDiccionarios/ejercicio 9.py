# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:06:15 2023

Ejercicio 9
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las
facturas se almacenarán en un diccionario donde la clave de cada factura será el número
de factura y el valor el coste de la factura. El programa debe preguntar al usuario si
quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una
nueva factura se preguntará por el número de factura y su coste y se añadirá al
diccionario. Si se desea pagar una factura se preguntará por el número de factura y se
eliminará del diccionario. Después de cada operación el programa debe mostrar por
pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

@author: gflogar
"""


facturas = {}

while True:
    print("¿Qué desea hacer?")
    print("1. Añadir una nueva factura")
    print("2. Pagar una factura existente")
    print("3. Terminar")

    opcion = input("Ingrese el número de la opción que desea: ")

    if opcion == "1":
        num_factura = input("Ingrese el número de factura: ")
        coste_factura = float(input("Ingrese el coste de la factura: "))

        facturas[num_factura] = coste_factura

        print("Factura añadida correctamente.")

    elif opcion == "2":
        num_factura = input("Ingrese el número de factura que desea pagar: ")

        if num_factura in facturas:
            del facturas[num_factura]
            print("Factura pagada correctamente.")
        else:
            print("La factura no existe.")

    elif opcion == "3":
        print("Gracias por utilizar el programa.")
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

    cantidad_cobrada = sum(facturas.values())
    cantidad_pendiente = 0

    for factura in facturas.values():
        cantidad_pendiente += factura

    print("Cantidad cobrada hasta el momento:", cantidad_cobrada)
    print("Cantidad pendiente de cobro:", cantidad_pendiente)