"""
Let's write a small console-driven app with a menu. Menu entries:
    1. Generate complex numbers
    2. Sort the numbers in increaseing order of modulo
    0. Exit
"""


def start():
    print("Welocome to seminar 02")

    while True:
        print("1. Generate complex numbers")
        print("2. Sort the numbers in increaseing order of modulo")
        print("0. Exit")

        opt = input(">")

        if opt == "1":
            pass
        elif opt == "2":
            pass
        elif opt == "0":
            return  # or break
        else:
            print("Bad command or file name")


start()
