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
    return str(z[0]) + "+" + str(z[1]) + "i"


def print_z(z: tuple) -> None:
    print(z[0], "+", z[1], "i")


# Functions that implement program requirements

z = create_z(1, 2)
print(z)
print(to_str(z))
print_z(z)
