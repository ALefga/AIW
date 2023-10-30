"""
Escribir un programa que pida palabras al usuario, 
los meta en una lista y luego indique que palabra es la más larga. (tiempo max 10 minutos)
"""
"""
palabras = []

cantidad = int(input("Ingrese la cantidad de palabras que desea ingresar: "))

for i in range(cantidad):
    palabra = input("Ingrese una palabra: ")
    palabras.append(palabra)

palabra_mas_larga = max(palabras, key=len)

print("La palabra más larga es:", palabra_mas_larga)
"""
lista =[]
mayor = ""
confirma =True

while confirma :
    palabra = input ("ingresa una palabra: ")
    lista.append(palabra)
    confirma = input("desea seguir poniendo palabras? (si/no)\t") == "si"

for i in lista:
    if len(lista[i]>len(mayor)):
        mayor = lista[i]
        
print("la palabra mas grande es: \n", mayor)