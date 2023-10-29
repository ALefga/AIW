"""
EJERCICIO 5:
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión.
"""
cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual en porcentaje: "))
num_anios = int(input("Ingrese el número de años de la inversión: "))

for i in range(num_anios):
    capital_obtenido = cantidad_invertir * (1 + interes_anual/100)*(i+1)
    print(f"Capital obtenido en el año {i+1}: {capital_obtenido}")
