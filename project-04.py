"""Adivinanza mediante imagenes"""

respuesta = ""

while True:
    try:

        respuesta = input("Ingrese el nombre de este animal")

        if respuesta == "perro":
            print("Correcto")

        else:

            print("Respuesta incorrecta, siga intentando")

    except ValueError:
        print("Ingrese una respuesta valida por favor")

        break
