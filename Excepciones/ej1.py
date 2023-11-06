while True:
    try:
        edad = int(input("Ingrese su edad: "))
        for i in range(1, edad+1):
            print("Ha cumplido", i, "años")
        break
    except ValueError:
        print("solo ingresa numero por favor!")
        continue