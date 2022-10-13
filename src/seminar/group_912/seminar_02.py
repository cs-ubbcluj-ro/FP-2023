from traceback import print_exc
import random

"""
Let's create a menu-driven application. This is the menu:
    1. Generate rational numbers
    2. Sort the list of numbers
    0. Exit
"""

"""
    Functions for Q numbers
"""


def create_q(num, denom=1):
    # TODO What about 1/0 !!
    return [num, denom]


def generate_q():
    """
    1. Ask user how many numbers
    2. Generate random num (in -10,10), denom (1, 20)
    3. Print the numbers
    3. Return the list of numbers
    """
    pass


def start():
    while True:
        print("1. Generate rational numbers")
        print("2. Sort the list of numbers")
        print("0. Exit")

        opt = input(">")  # by default reads str

        # print(type(opt))
        if opt == "1":
            pass
        elif opt == "2":
            pass
        elif opt == "0":
            return  # or break
        else:
            print("Bad command or file name :)")


start()
