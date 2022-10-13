"""
Let's write a menu-driven application to work with points in 2D space.
    1. Generate points in 2D space
    2. Sort the points by distance from center
    0. Exit
"""


def start():
    while True:
        print("1. Generate points in 2D space")
        print("2. Sort the points by distance from center")
        print("0. Exit")

        opt = input(">")
        # print(type(opt))

        if opt == "1":
            pass
        elif opt == "2":
            pass
        elif opt == "0":
            return  # or break
        else:
            print("Bad command (or file name) :)")


start()
