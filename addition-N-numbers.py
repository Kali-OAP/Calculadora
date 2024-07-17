
maximum = input("Insert a max number: ")

maximum = int(maximum)
addition = 0
num = 2

while num <= maximum:

    prime_number = True  # By default it's True but this can't change with the "if"
    validate = 2  # This helps to validate if the number it's prime
    while validate < num:
        if num % validate == 0:
            prime_number = False
            break
        validate += 1
    if prime_number:  # If it's prime this means addition = 0 plus (+) num = 2
        addition += num

    num += 1

print(f"The result of the addition until {maximum} it's {addition}")
