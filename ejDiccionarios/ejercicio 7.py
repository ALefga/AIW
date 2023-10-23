# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:20:59 2023

Ejercicio 7
Escribir un programa que cree un diccionario simulando una cesta de la compra. El
programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que
el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y
el coste total, con el siguiente formato
Lista de la compra
Artículo 1
Artículo 2 
Artículo 3 
… 
Total 

@author: gflogar
"""


lista_de_compra = {}


while True:
    articulo = input("nombre del artículo o 'terminar' para salir: ")
    if articulo.lower() == 'terminar':
        break

    precio = float(input("precio del artículo: "))
    lista_de_compra[articulo] = precio


print("\nLista de la compra:")
total = 0
for item, price in lista_de_compra.items():
    print(f"{item}: €{price}")
    total += price

print(f"Total: €{total}")
