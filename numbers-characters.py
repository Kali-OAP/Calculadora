"""This it's useful to know how many numbers have a string"""


word = ""

while True:
    if not word:

        result = input("Insert a sentence or word: ")

    if result.lower == "exit":

        break

    else:
        word = result
        lenn = len(word)
        print(f"The sentence or word has: {lenn} characters")
        break
