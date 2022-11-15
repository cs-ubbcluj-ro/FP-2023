"""
Created on Sep 30, 2016

@author: Istvan Czibula / Arthur Molnar
"""
from math import gcd

"""
Create a calculator program for rational numbers with the following functionalities:
    + add a rational number to the calculator
    u undo the last operation
    x exit
"""


# ----------------------#
# Non-UI functions here #
# ----------------------#

# Functions to handle rational numbers


def create_rational(num, denom):
    if denom == 0:
        raise ValueError("Fraction denominator 0")
    d = gcd(num, denom)
    num = num // d
    denom = denom // d
    return [num, denom]


def get_numerator(q):
    return q[0]


def get_denominator(q):
    return q[1]


def add(q1, q2):
    """
    Return the sum of two rational numbers.
    input: q1, q2 - rational numbers operands
    return the result
    """
    return create_rational(get_numerator(q1) * get_denominator(q2) +
                           get_numerator(q2) * get_denominator(q1),
                           get_denominator(q1) * get_denominator(q2))


def to_str(q):
    return str(get_numerator(q)) + "/" + str(get_denominator(q))


# Functions to handle the calculator


def create_calculator():
    """
    Create a new calculator
    post: the current total equal 0/1
    return calculator status
    """
    return {'val': create_rational(0, 1), 'history': []}


def get_total(calc):
    return calc['val']


def set_total(calc, q):
    calc['val'] = q


def add_calculator(calc, q):
    """
    add a rational number to the current total
    input: calc - calculator
           q - rational number
    output: q is added to the calculator
    """
    calc_total = get_total(calc)
    # Record the operation for undo
    history = calc['history']
    history.append(calc_total)
    # Set current calculator value
    set_total(calc, add(calc_total, q))


def undo_calc(calc):
    """
    :param calc: The calculator to undo
    :return: 0 if successful, -1 if nothing to undo
    """
    history = calc['history']
    if len(history) == 0:
        # Return statement signals operation failure
        return -1
    calc['val'] = history[-1]
    history.pop()
    # Return statement signals operation success
    return 0


# -----------------------#
# Only UI functions here #
# -----------------------#


def print_menu():
    print("Calculator menu:")
    print("   + add a rational number")
    print("   u undo last operation")
    print("   x close the calculator")


def add_calc_ui(calc):
    """
      Read a rational number and add to the current total
      calc - calculator
    """
    m = input("Give nominator:")
    n = input("Give denominator:")
    add_calculator(calc, create_rational(int(m), int(n)))


def undo_calc_ui(calc):
    success = undo_calc(calc)
    if success < 0:
        print('Nothing to undo!')


def run():
    """
      Implement the user interface
    """
    commands = {'+': add_calc_ui, 'u': undo_calc_ui}
    calculator = create_calculator()

    finish = False
    while not finish:
        print('Total= ' + to_str(get_total(calculator)))
        print_menu()
        m = input().strip()

        if m in commands.keys():
            commands[m](calculator)
        elif m == 'x':
            return
        else:
            print("Invalid command")


"""
Program entry point
"""
run()
