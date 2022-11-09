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

def create_q(num, den: int = 1):
    """
    Create Rational number
    :param num:
    :param den:
    :return: The number, or None if number is invalid
    """
    if den == 0:
        return None
    # return [num, den]
    return {"num": num, "den": den}


def get_num(q):
    # return q[0]
    return q["num"]


def get_den(q):
    # return q[1]
    return q["den"]


def add_q(q1, q2):
    num = get_num(q1) * get_den(q2) + get_num(q2) * get_den(q1)
    den = get_den(q1) * get_den(q2)
    g = gcd(num, den)
    return create_q(num // g, den // g)


def to_str(q):
    if get_den(q) == 1:
        return str(get_num(q))
    return str(get_num(q)) + "/" + str(get_den(q))


# -----------------------#
# Only UI functions here #
# -----------------------#

def add_rational(total):
    num = int(input("enter numerator:"))
    den = int(input("enter denominator:"))

    q = create_q(num, den)
    if q is None:
        print("Invalid rational number")
        return

    return add_q(q, total)


def print_menu():
    print("+ add a rational number to the calculator")
    print("u undo the last operation")
    print("x exit")


def start():
    total = create_q(0)
    while True:
        print_menu()
        print("Total: " + to_str(total))
        opt = input(">")

        if opt == "+":
            total = add_rational(total)
        elif opt == "x":
            break
        else:
            print("Bad user option")


if __name__ == "__main__":
    start()
