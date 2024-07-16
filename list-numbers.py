
maximum = input("Insert a value to make your list: ")

maximum = int(maximum)
list_numbers = []
num = 1


while num <= maximum:
    list_numbers.append(num)
    num += 1

    print(
        f"The natural numbers until the value you insert it's {list_numbers}")
