# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:08:43 2023

@author: gflogar
"""

num1=int(input("Dime un número"))
num2=int(input("Dime un número"))
num3=int(input("Dime un número"))
if num1 > num2 and num1 > num3:
    print ("El valor mayor es :", num1)
elif num2 > num1 and num2 > num3:
    print ("El valor mayor es :", num2)
else:
    print ("El valor mayor es :", num3)