"""
command driven calculator
    add 1/2,4/5,99/98,45,1/0,...
    exit
"""
from lecture.live.lecture_07.domain.rational_list import create_q
from lecture.live.lecture_07.functions.calculator import add_q, to_str


def add_ui(total, param: str):
    """
    Add the numbers to the calculator
    :param param:
    :return: The new value of the calculator
    Raise ValueError if param contains a non-number, a 0-denominator, missing numerator
    """
    numbers_str = param.split(",")
    for number in numbers_str:
        if number.find("/") == -1:
            q = create_q(int(number))
        else:
            # FIXME crash if multiple /
            num, denom = number.split("/")
            if len(num.strip()) == 0:
                raise ValueError("Numerator missing")
            q = create_q(int(num), int(denom))
        total = add_q(total, q)
    return total

#
# def test_add_ui():
#     total = create_q(0)
#     assert add_ui(total, "0") == create_q(0)
#     assert add_ui(total, "1") == create_q(1, 1)
#     assert add_ui(total, "1/2,1/2") == create_q(1)
#     assert add_ui(total, "1/2,1/3") == create_q(5, 6)
#     assert add_ui(total, "1/2,-1/3") == create_q(1, 6)
#
#     # Check that a ValueError is actually raised
#     try:
#         add_ui(total, "1/2,1/0")
#         assert False
#     except ValueError:
#         assert True
#
#     try:
#         add_ui(total, "1/2,1/e")
#         assert False
#     except ValueError:
#         assert True
#
#     try:
#         add_ui(total, "1/2,/6")
#         assert False
#     except ValueError:
#         assert True


def start():
    total = create_q(0)
    while True:
        print(to_str(total))
        command = input(">")
        if command.startswith("add"):
            total = add_ui(total, command[4:])
        elif command.startswith("exit"):
            return
        else:
            print("Invalid command")


start()
