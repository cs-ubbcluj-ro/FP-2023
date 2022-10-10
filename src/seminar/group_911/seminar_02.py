"""
Let's write a menu-driven application. What does the menu look like?
    1. Generate (random) person names
    2. Exit
"""
import random


def generate_names():
    count = int(input("How many names to generate? "))  # int() converts to integer

    family_names = ["Albu", "Pop", "Gheorghe", "Morar", "Negrea", "Bodnar"]  # list()
    given_names = ["Anca", "Elisa", "Ionut", "Vasile", "Ioana", "Rares"]
    result = []

    for i in range(count):
        family_name = random.randint(0, len(family_names) - 1)
        given_name = random.randint(0, len(given_names) - 1)
        name = family_names[family_name] + " " + given_names[given_name]
        result.append(name)

    # Let's print out the names
    print(result)
    return result


def start():
    print("Welcome to seminar 2!")

    while True:
        print("1. Generate (random) person names")
        print("2. Exit")

        opt = input(">")

        if opt == "1":
            generate_names()
        elif opt == "2":
            return  # break would have also been acceptable
        else:
            print("Bad command or file name")


start()
