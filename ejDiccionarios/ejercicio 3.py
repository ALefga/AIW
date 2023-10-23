# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:30:53 2023

Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un
mensaje informando de ello.
Fruta                   Precio
Plátano                 1.35
Manzana                 0.80
Pera                    0.85
Naranja                 0.70

@author: gflogar
"""


precios_frutas = {
    "platano": 1.35,
    "manzana": 0.80,
    "pera": 0.85,
    "naranja": 0.70
}


fruta = input("Ingrese el nombre de la fruta: ")
kilos = float(input("Ingrese la cantidad en kilos: "))


if fruta in precios_frutas:
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es: {precio_total} euros")
else:
    print("Lo siento, la fruta ingresada no está en el diccionario de precios.")
