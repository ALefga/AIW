# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:27:59 2023

Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene
<edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

@author: gflogar
"""

nombre = input("Por favor, ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
direccion = input("Ingresa tu dirección: ")
telefono = input("Ingresa tu número de teléfono: ")

informacion_usuario = {
    "nombre": nombre,
    "edad": edad,
    "dirección": direccion,
    "teléfono": telefono
}

print(f"{informacion_usuario['nombre']} tiene {informacion_usuario['edad']} años, vive en {informacion_usuario['dirección']} y su número de teléfono es {informacion_usuario['teléfono']}")
