"""
Escribir un programa que pida enteros al usuario, y los meta en una lista para que
luego muestre la suma de esos elementos y la multiplicación de los elementos. (tiempo max 10 minutos)
"""

lista = []
seguir =True
totalsum = 0
totalmul = 1
while seguir:
    numero =int(input("introduce un numero: "))
    lista.append(numero)
    seguir = input ("quieres seguir añadiendo numero? ") ("si/no") == "si"
for x in lista:
    totalsum += x
    totalmul += x
print ("total suma:", totalsum, "total multiplicacion:", totalmul)