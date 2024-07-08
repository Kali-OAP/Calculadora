"""Projecto python-2"""

while True:
    try:
        numero = int(input("Ingrese un número entero positivo"))
        if numero > 0:

            break

        else:
            print("Ingrese un número entero por favor")

    except ValueError:

        print("Número invalido, por favor introduzca un número entero positivo")
