"""
EJERCICIO 3:
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por comas.

"""
numero = int(input("Ingrese un número entero positivo: "))
impares = ""
for i in range(1, numero+1, 2):
    impares += str(i) + ", "
print("Los números impares desde 1 hasta", numero, "son:", impares[:-2])