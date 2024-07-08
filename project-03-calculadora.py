numero = input("Ingresa un valor inicial")
numero2 = input("Ingresa un valor final")

numero = int(numero)
numero2 = int(numero2)

multiplicacion = numero * numero2
resta = numero - numero2
suma = numero + numero2
mensaje = f"""
Para los valores {numero} y {numero2} se
concluye en un resultado de {multiplicacion} en la multiplicacion
un resultado de {resta} en la resta y un resultado de {suma} en la suma

"""
print(mensaje)
