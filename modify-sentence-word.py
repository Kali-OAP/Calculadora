"""Modify a word or sentence"""


word = ""


while True:
    if not word:
        sentence = input(
            "Insert a sentence or word that you want or exit to leave: ")

    if sentence.lower() == "exit":
        break

    try:

        word = sentence
        print(f"The word has been modified: {word[::-1]}")
        break

    except ValueError:
        print("Insert a number")
        continue
