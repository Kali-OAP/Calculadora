import random

nombre = input(
    "Ingrese los nombres de los participantes por favor, con comas")
print("Registrando al usuario" + nombre + "!")

lista_nombres = nombre.split(',')

ganador = random.choice(lista_nombres)

print(f"El ganador es: {ganador.strip()}")
