"""
Let's create a menu-driven application. This is the menu:
    1. Generate rational numbers
    2. Sort the list of numbers
    0. Exit
"""


def start():
    while True:
        print("1. Generate rational numbers")
        print("2. Sort the list of numbers")
        print("0. Exit")

        opt = -1
        try:
            opt = int(input(">"))  # by default reads str
        except ValueError as ve:
            print(ve)

        # print(type(opt))
        if opt == 1:
            pass
        elif opt == 2:
            pass
        elif opt == 0:
            return  # or break
        else:
            print("Bad command or file name :)")


start()
