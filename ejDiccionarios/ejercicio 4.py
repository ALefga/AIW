# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:37:04 2023

Ejercicio 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del
mes.

@author: gflogar
"""

import datetime


meses = {
    1: 'enero',
    2: 'febrero',
    3: 'marzo',
    4: 'abril',
    5: 'mayo',
    6: 'junio',
    7: 'julio',
    8: 'agosto',
    9: 'septiembre',
    10: 'octubre',
    11: 'noviembre',
    12: 'diciembre'
}


fecha_str = input("Ingresa una fecha en formato dd/mm/aaaa: ")


try:
    fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")

    dia = fecha.day
    mes_numero = fecha.month
    año = fecha.year


    mes = meses[mes_numero]


    print(f"La fecha es: {dia} de {mes} de {año}")
except ValueError:
    print("Formato de fecha incorrecto. Asegúrate de ingresar la fecha en formato dd/mm/aaaa.")

