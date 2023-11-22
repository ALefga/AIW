# EJERCICIO 7:
# Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contrasena_correcta = "contrasena"

while True:
    contrasena = input("Introduce la contraseña: ")
    if contrasena == contrasena_correcta:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
