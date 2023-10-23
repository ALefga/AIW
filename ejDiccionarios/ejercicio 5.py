# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:00:45 2023

Ejercicio 5
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de
un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los
créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus
créditos. Al final debe mostrar también el número total de créditos del curso.

@author: gflogar
"""


creditos_asig = {'Matemáticas': 6, 'Física': 4, 'Química': 5}


for asignatura, creditos in creditos_asig.items():
    print(f"{asignatura} tiene {creditos} créditos")


total_creditos = sum(creditos_asig.values())
print(f"El número total de créditos del curso es: {total_creditos}")
