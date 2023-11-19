"""
Calculator UI as menu
"""
from src2023.lecture.livecoding.lecture07.calc.calculator import *


def printMenu():
    print("Calculator")
    print("\t+ add")
    print("\tu undo")
    print("\tx exit")


def calculator_add_ui(calculator):
    num = int(input("numerator="))
    den = int(input("denominator="))
    q = create_q(num, den)
    add_calc(calculator, q)


def calculator_undo_ui(calc):
    undo_calc(calc)


def start():
    functions = {"+": calculator_add_ui, "u": calculator_undo_ui}
    calc = create_calc()

    while True:
        printMenu()
        print("calculator value = " + to_str(get_calc_value(calc)))
        opt = input(">")

        if opt in functions:
            try:
                functions[opt](calc)  # () -- function call operator
            except ValueError as ve:
                print(ve)
        elif opt == "x":
            break
        else:
            print("Invalid menu entry")


start()
