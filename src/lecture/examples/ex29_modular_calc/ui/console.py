"""
  The user interface of the calculator
  Contains functions related to the user interaction (console)
"""
from src.lecture.examples.ex29_modular_calc.domain.calculator import \
    calculator_add, undo, get_calculator_total, get_undo_list, set_calculator_total, reset_calc
from src.lecture.examples.ex29_modular_calc.domain.rational import create_rational


def print_menu():
    """
      Print out the main menu of the calculator
    """
    print("Calculator menu:")
    print("   + for adding a rational number")
    print("   c to clear the calculator")
    print("   u to undo the last operation")
    print("   x to close the calculator")


def print_current(calc):
    """
      Print the current total
    """
    print("Total:", get_calculator_total(calc))


def run():
    """
      Implement the user interface
    """
    calc = reset_calc()
    finish = False
    print_current(calc)
    while not finish:
        print_menu()
        m = input().strip()
        if m == 'x':
            finish = True
        elif m == '+':
            m = input("Give numerator:")
            n = input("Give denominator:")
            try:
                calculator_add(calc, create_rational(int(m), int(n)))
                print_current(calc)
            except ValueError:
                print("Enter integers for m, n, with not null n")
        elif m == 'c':
            calc = reset_calc()
            print_current(calc)
        elif m == 'u':
            try:
                undo(calc)
                print_current(calc)
            except ValueError as ve:
                print(ve)
        else:
            print("Invalid command")
