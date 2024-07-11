"""This gonna help to know if a number it's even or odd"""

even = int(input("Insert a number: "))

if even % 2 == 0:

    print(f"The result of {even} it's even")

else:
    print(f"The result of {even} it's odd")


# Everything I tried:

# even = int(input("Please insert a number: "))

# for result in range(0, 11, 2):

# while True:
#     if even == result:
#         print(f"The result it's even {even}")
#         break
#     elif even != result:
#         print(f"the result it's odd {even}")
#         break

# even = input("Insert a number: ")

# try:
#     numbers == int(even)

# except ValueError:
#     print("Insert a valid number")
# if even == numbers:
#     print("The result it's even")
# while True:
#     if not numbers:
#         user = input(
#             "If you wanna leave enter 'exit' or Insert a number to know if it's even or odd: ")

#         if user.lower == "exit":
#             break
#     try:
#         numbers = int(user)

#     except ValueError:
#         print("Insert an integer number greater than 0")
