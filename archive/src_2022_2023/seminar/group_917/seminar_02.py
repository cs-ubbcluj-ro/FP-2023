"""
Let's write a small console-driven app with a menu. Menu entries:
    1. Generate complex numbers
    2. Sort the numbers in increaseing order of modulo
    0. Exit
"""
import random


#
# Complex number functions
#

def create_z(real: int, imag: int):
    """
    Create a complex number
    :param real: Its real part
    :param imag: Its imaginary part
    :return: Return a dict representing the number
    """
    return {"real": real, "imag": imag}
    # return [real, imag]


def get_real(z):
    return z["real"]
    # return z[0]


def get_imag(z):
    return z["imag"]
    # return z[1]


def z_mod(z):
    return (get_real(z) ** 2 + get_imag(z) ** 2) ** (1 / 2)


def z_str(z):
    return str(get_real(z)) + "+" + str(get_imag(z)) + "i"


#
# Program functions
#

def generate_z():
    count = int(input("How many numbers to generate? "))
    number_list = []  # empty list, list() also works

    for i in range(count):
        real = random.randint(-10, 10)
        imag = random.randint(-10, 10)
        number_list.append(create_z(real, imag))

    # print(number_list)
    for z in number_list:
        print(z_str(z))
    return number_list


def sort_numbers(numbers_list: list):
    pass


def start():
    print("Welocome to seminar 02")

    complex_numbers = []

    while True:
        print("1. Generate complex numbers")
        print("2. Sort the numbers in increaseing order of modulo")
        print("0. Exit")

        opt = input(">")

        if opt == "1":
            complex_numbers = generate_z()
        elif opt == "2":
            sort_numbers(complex_numbers)
        elif opt == "0":
            return  # or break
        else:
            print("Bad command or file name")


start()
