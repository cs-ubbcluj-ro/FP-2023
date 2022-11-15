"""
  Calculator module, contains functions related to the calculator
"""
from src.lecture.examples.ex29_modular_calc.domain.rational import add, create_rational

'''
    Calculator state
'''


def get_calculator_total(calc):
    return calc[0]


def set_calculator_total(calc, total):
    calc[0] = total


def get_undo_list(calc):
    return calc[1]


def reset_calc():
    return [create_rational(0), []]


"""
    Other calculator operations
"""


def undo(calc):
    """
      Undo the last user operation
      post: restore the previous current total
    """
    if len(get_undo_list(calc)) == 0:
        raise ValueError("No more undos!")

    set_calculator_total(calc, get_undo_list(calc)[-1])
    get_undo_list(calc).pop()


def calculator_add(calc, q):
    """
      add a rational number to the current total
      a, b integer number, b<>0
      post: add a/b to the current total
    """
    # add the current total to the undo list

    get_undo_list(calc).append(get_calculator_total(calc))
    set_calculator_total(calc, add(get_calculator_total(calc), q))


def test_calculator_add():
    """
      Test function for calculator_add
    """
    c = reset_calc()
    assert get_calculator_total(c) == create_rational(0)
    calculator_add(c, create_rational(1, 2))
    assert get_calculator_total(c) == create_rational(1, 2)
    calculator_add(c, create_rational(1, 3))
    assert get_calculator_total(c) == create_rational(5, 6)
    calculator_add(c, create_rational(1, 6))
    assert get_calculator_total(c) == create_rational(1)


def test_undo():
    """
      Test function for undo
    """
    c = reset_calc()
    calculator_add(c, create_rational(1, 3))
    undo(c)
    assert get_calculator_total(c) == create_rational(0)
    c = reset_calc()
    calculator_add(c, create_rational(1, 3))
    calculator_add(c, create_rational(1, 3))
    calculator_add(c, create_rational(1, 3))
    undo(c)
    assert get_calculator_total(c) == create_rational(2, 3)
