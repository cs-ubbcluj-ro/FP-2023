"""
What we should learn here:
    basic Python types: int, str, boolean, float
    compound types: dict, list, tuple
    Python 3 elements: loops, writing functions, specifications, console I/O

Problem statement:
    Manage a list of complex numbers
        Display all numbers to the console
        Add a number from the console
        Add a random number
        Sort by number modulo
        Exit the program :)
"""


# TODO Implement remaining functionalities

# Functions that deal with complex numbers

# z = 1 + 2*i => z_tuple = (1,2)

def create_z(real: int, imag: int) -> tuple:
    """
    Creates a complex number in the form (real + imag * i)
    :param real: The real part.
    :param imag: The imaginary part.
    :return: Returns the new number as a tuple
    """
    return real, imag


def to_str(z: tuple) -> str:
    # TODO Write specification for this function
    if z[1] == 0:
        return str(z[0])
    if z[0] == 0:
        return str(z[1]) + "i"
    if z[1] < 0:
        return str(z[0]) + str(z[1]) + "i"
    return str(z[0]) + "+" + str(z[1]) + "i"


def print_z(z: tuple) -> None:
    print(z[0], "+", z[1], "i")


# Functions that implement program requirements

data = [create_z(1, 2), create_z(1, -1), create_z(0, 0), create_z(45, 0)]  # data = list()
flag = True
while flag:
    print("1. Add a complex number")
    print("2. Display all numbers")
    print("0. Exit")

    option = input(">")
    if option == "1":
        # TODO Parse numbers in the (a + bi) format
        # TODO Program crash on incorrect input
        z_real = int(input("real part: "))
        z_imag = int(input("imag part: "))
        z = create_z(z_real, z_imag)
        data.append(z)

    elif option == "2":
        print("The numbers are: ")
        # print(data)

        for z in data:
            print(to_str(z), end=" ")  # end is a named Python parameter
        print("")

        # print(list(map(to_str, data)))

        # for i in range(0, len(data)):
        #     # range(0,5) -> 0, 1, 2, 3, 4
        #     print(to_str(data[i]))
    elif option == "0":
        flag = False
        print("bye!")
    else:
        print("Bad command or file name")

# z = create_z(1, 2)
# print(z)
# print(to_str(z))
# print_z(z)
