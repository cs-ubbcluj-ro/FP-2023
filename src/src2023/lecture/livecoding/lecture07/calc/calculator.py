# import src.src2023.lecture.livecoding.lecture07.domain.rational_as_list
from src2023.lecture.livecoding.lecture07.domain.rational_as_list import *


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
    return {"value": create_q(0), "history": [create_q()]}


def get_calc_value(calc):
    return calc["value"]


def add_calc(calc, q):
    """
    Add a new value to the calculator
    :param calc: The calc
    :param q: New value
    """
    new_value = add(get_calc_value(calc), q)
    calc["value"] = new_value
    calc["history"].append(new_value)
    print(calc["history"])


def undo_calc(calc):
    """
    Undo the last operation of calculator
    Raise ValueError in case there is no undo available
    """
    if len(calc["history"]) == 1:
        raise ValueError("No more undos")
    last_value = calc["history"].pop()
    calc["value"] = calc["history"][-1]
