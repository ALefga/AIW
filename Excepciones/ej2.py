while True:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        impares = ""
        if numero<0:
            print("ingresa un numero mayor a 0")
            continue
        for i in range(1, numero+1, 2):
            impares += str(i) + ", "
            print("Los números impares desde 1 hasta", numero, "son:", impares[:-2])
        break
    except ValueError:
        print("Ingresa un numero, por favor")
        continue