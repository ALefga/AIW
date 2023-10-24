# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:05:55 2023

Ejercicio 6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
contenido del diccionario.

@author: gflogar
"""

persona = {}

while True:
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    sexo = input("Ingrese el sexo: ")
    telefono = input("Ingrese el teléfono: ")
    correo = input("Ingrese el correo electrónico: ")

    persona['Nombre'] = nombre
    persona['Edad'] = edad
    persona['Sexo'] = sexo
    persona['Teléfono'] = telefono
    persona['Correo'] = correo

    print("Información de la persona:")
    for clave, valor in persona.items():
        print(f"{clave}: {valor}")





