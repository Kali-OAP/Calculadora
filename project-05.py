"""Calculator"""

import math

# In this calculator you insert one value and then an operation, after that you have to choose another one value

print("Welcome, to calculate your operation please insert 2 values and an operation like; subtraction( - ), addition( + ), multiplication( * ), y division( / )")


def low_to_integer(result):
    if result.is_integer():
        return int(result)


n1 = ""

while True:

    if not n1:

        number = input(
            "Enter an integer number, if you want square root please enter square: ")

    if number.lower() == "exit":

        break

    elif number.lower() == "square":

        sqrt = int(input("Enter a number: "))

        if sqrt > 0:

            print(f"The result is: {math.sqrt(sqrt)}")
        continue
    try:
        n1 = int(number)

    except ValueError:
        print("Error, please insert an integer number, or a float")
        continue

    op = input("Insert an symbol operation: ")

    if op.lower() == "exit":
        break

    if op not in ['*', '-', '+', '/', '^']:
        print("Invalid, please insert an valid operation")
        continue

    n2 = input("Enter the next integer number: ")

    if n2.lower() == "exit":

        break

    try:
        n2 = int(n2)

    except ValueError:
        print("Error, insert an integer number or a float")

        continue

    if op.lower() == "+":
        n1 += n2
        print(f"The result is: {n1}")

        break

    elif op.lower() == "*":
        n1 *= n2
        print(f"The result is: {n1}")
        break

    elif op.lower() == "-":
        n1 -= n2
        print(f"The result is: {n1}")
        break

    elif op.lower() == "/":

        if n1 or n2 == 0:
            print("Invalid value, please insert a number greater than zero")
            break

        else:
            n1 /= n2
            print("The result is: {n1}")
            break

    elif op.lower() == "^":
        result = math.pow(n1, n2)
        print(f"The result is:  {low_to_integer(result)}")
        break

    else:
        print("Unknown character, please insert a number")
        continue
