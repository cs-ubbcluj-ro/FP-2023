"""
Create a calculator program for rational numbers with the following functionalities:
    + add a rational number to the calculator
    u undo the last operation
    x exit
"""
from math import gcd


# ----------------------#
# Non-UI functions here #
# ----------------------#

# 2 entities in our program
# - rational number (numerator, denominator)
# - calculator (current value, value history for undo)

# code section for rational number
# 1/3 => (1,3) - tuple
def create_q(num: int, den: int = 1):
    """
    Create a rational number
    :param num: Numerator
    :param den: Denominator, <> 0
    :return: The number
    Raises ValueError in case den == 0
    """
    if den == 0:
        raise ValueError("Cannot create rational number with den == 0")
    g = gcd(num, den)
    # return num // g, den // g
    return {"num": num // g, "den": den // g}


def get_num(q) -> int:
    """
    Return numerator of number q
    """
    # return q[0]
    return q["num"]


def get_den(q) -> int:
    """
    Return denominator of number q
    """
    # return q[1]
    return q["den"]


def add(q1, q2):
    """
    Add rational number q1 and q2
    :param q1:
    :param q2:
    :return: New rational number q1 + q2
    """
    num = get_num(q1) * get_den(q2) + get_num(q2) * get_den(q1)
    den = get_den(q1) * get_den(q2)
    return create_q(num, den)


def to_str(q) -> str:
    # TODO fix +/-1 and so on
    # FIXME we need to fix this
    if get_den(q) == 1:
        return str(get_num(q))
    return str(get_num(q)) + "/" + str(get_den(q))


# code section for calculator
# abstraction - calculator should not rely on how a rational
# number is represented => we need an interface to rational numbers

def create_calc():
    """
    Create the calculator instance
    """
    # initial value in calculator is 0
    # history stack is used for undoing operations
    return {"value": create_q(0), "history": []}


def add_calc(q):
    pass


def undo_calc():
    """
    Undo the last operation of calculator
    Raise ValueError in case there is no undo available
    """
    pass


# -----------------------#
# Only UI functions here #
# -----------------------#

def print_menu():
    print("Calculator menu")
    print("\t + add to calc")
    print("\t u undo last operation")
    print("\t x exit calc")


def start():
    """
    What should start do here, and in A5?
        1. Print main menu
        2. Read user options
        3. Call the function that solves the user's request
    """
    calc = create_calc()

    while True:
        print_menu()
        opt = input(">")  # this is an str

        if opt == "+":
            pass
        elif opt == "u":
            pass
        elif opt == "x":
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    start()

    # try:
    #     q = create_q(2, 5)
    #
    #     """
    #     q1 = create_q(7, 0) -- order of operations
    #         1. create_q() is called
    #         2. create_q() exists with exception ValueError
    #            create_q() does not return a value!
    #         3. the assignment "q = ..." does not run\
    #         4. "q"is undefined
    #         5. The "except"block runs
    #
    #     """
    #     q1 = create_q(-7, 2)
    #     q2 = create_q(7, -2)
    #     print(to_str(add(q1, q2)))
    # except ValueError as ve:
    #     # ve is the alias of the exception variable
    #     print(ve)
