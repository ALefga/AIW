"""
EJERCICIO 4:
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
numero = int(input("Ingrese un número entero positivo: "))
cuenta_regresiva = ""
for i in range(numero, -1, -1):
    cuenta_regresiva += str(i) + ","
print(cuenta_regresiva[:-1])