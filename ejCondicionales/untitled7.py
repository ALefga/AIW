# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:11:52 2023

@author: gflogar
"""


dia = input("dime un dia en minuscula:")
if dia == "lunes":
    print ("Que tengas un buen comienzo de semana")
elif dia == "viernes":
    print ("feliz viernes")
elif dia == "sabado" or dia == "domingo":
    print ("buen fin de semana")
else:
    print("dia normal")