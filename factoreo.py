"""Factorial"""

import math  # I use  math because it has math.factorial

factor = ""

while True:
    if not factor:
        factorial = input(
            "Enter exit if you wanna leave or insert an number to progress, this number has to be greater than 0, and positive: ")

    if factorial.lower() == "exit":
        print("Leaving...")
        break

    try:
        factor = int(factorial)

    except ValueError:
        print("Insert a number")

    if factor > 0:

        print(math.factorial(factor))

        break
    else:
        print("Please insert a number greater than 0")
        continue
