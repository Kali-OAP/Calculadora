"""Calculadora mas avanzada Proyecto"""

import math

# Una calculadora en la cual se ingresen 1 valor luego la operacion, y luego otro valor

print("Bienvenidos, a la calculadora, las operaciones son; resta( - ), suma( + ), multiplicacion( * ), y division( / )")


def bajar_a_entero(resultado):
    if resultado.is_integer():
        return int(resultado)


n1 = ""

while True:

    if not n1:

        numero = input(
            "Ingrese un numero o si desea la raiz cuadra, ingrese raiz: ")

    if numero.lower() == "salir":

        break
    elif numero.lower() == "raiz":

        raizc = int(input("Ingrese un numero: "))

        if raizc > 0:

            print(f"Su resultado es: {math.sqrt(raizc)}")
        continue
    try:
        n1 = int(numero)

    except ValueError:
        print("Error, ingrese un valor valido, enteros")
        continue

    op = input("Ingrese un signo de operacion: ")

    if op.lower() == "salir":
        break

    if op not in ['*', '-', '+', '/', '^']:
        print("Invalido, ponga una operacion valida")
        continue

    n2 = input("Ingresa el siguiente numero: ")

    if n2.lower() == "salir":

        break

    try:
        n2 = int(n2)

    except ValueError:
        print("Error, Ingrese un valor valido, enteros")

        continue

    if op.lower() == "+":
        n1 += n2
        print(f"El resultado es {n1}")

        break

    elif op.lower() == "*":
        n1 *= n2
        print(f"El resultado es: {n1}")
        break
    elif op.lower() == "-":
        n1 -= n2
        print(f"Su resultado es: {n1}")
        break

    elif op.lower() == "/":
        n1 /= n2
        print(f"Su resultado es: {n1}")
        break

    elif op.lower() == "^":
        resultado = math.pow(n1, n2)
        print(f"Su resultado es:  {bajar_a_entero(resultado)}")
        break

    else:
        print("Valor incorrecto, ingrese lo requerido")
        continue
