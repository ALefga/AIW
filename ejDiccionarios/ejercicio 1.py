# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:20:14 2023

Ejercicio 1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$',
'Yen':'Y'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de
aviso si la divisa no está en el diccionario.

@author: gflogar
"""


diccionario = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
divisa = input("Por favor, ingrese una divisa: ")

if divisa in diccionario:
    simbolo = diccionario[divisa]
    print(f"El símbolo de {divisa} es: {simbolo}")
else:
    print("La divisa ingresada no está en el diccionario.")
