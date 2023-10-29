"""
EJERCICIO 7:
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.
"""
contraseña = "contraseña"
entrada = input("Introduce la contraseña: ")
while entrada != contraseña:
    entrada = input("Contraseña incorrecta. Introduce la contraseña nuevamente: ")
print("Contraseña correcta. Acceso concedido.")
