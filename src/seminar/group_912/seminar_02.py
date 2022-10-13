from traceback import print_exc
import random
import math

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
    gcd = math.gcd(num, denom)
    return [num // gcd, denom // gcd]


def generate_rationals_v2():
    """Function used in order to generate rational numbers"""
    numbers_list = []

    nr_numbers = input("Please input how many numbers you'd like to store.")
    nr_numbers = int(nr_numbers)

    for iterator in range(0, nr_numbers):
        num = random.randint(-10, 10)
        denom = random.randint(1, 20)
        numbers_list.append(create_q(num, denom))

    for q in numbers_list:
        print(tranform_to_string(q))
    return numbers_list


def tranform_to_string(rational_nr_list):
    """
    Function used in order to represent the rational number as a string

    :param rational_nr_list: a list of num and denom
    :return: a string
    """
    num, denom = rational_nr_list
    result = num / denom
    int_result = int(result)

    if result == int_result:
        string_to_be_returned = str(result)
    else:
        string_to_be_returned = f"{num} / {denom}"

    return string_to_be_returned


def start():
    while True:
        print("1. Generate rational numbers")
        print("2. Sort the list of numbers")
        print("0. Exit")

        opt = input(">")  # by default reads str

        # print(type(opt))
        if opt == "1":
            generate_rationals_v2()
        elif opt == "2":
            pass
        elif opt == "0":
            return  # or break
        else:
            print("Bad command or file name :)")


start()
