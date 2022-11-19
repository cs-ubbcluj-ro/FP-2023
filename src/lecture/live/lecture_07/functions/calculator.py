from lecture.live.lecture_07.domain.rational_list import *
from math import gcd


def add_q(q1, q2):
    num = get_num(q1) * get_den(q2) + get_num(q2) * get_den(q1)
    den = get_den(q1) * get_den(q2)
    g = gcd(num, den)
    return create_q(num // g, den // g)


def add_qs(numbers: list):
    """
    Add the rational nrs in the list
    :param numbers: List of Q numbers
    :return: The sum of numbers
    """
    total = create_q(0)
    for q in numbers:
        total = add_q(total, q)
    return total


def test_add_qs():
    assert add_qs([]) == create_q(0)

    q1 = create_q(1, 3)
    q2 = create_q(2, 3)
    q3 = create_q(1, 6)
    q4 = create_q(1)
    q5 = create_q(0)
    assert add_qs([q1]) == q1
    assert add_qs([q1, q2]) == create_q(1, 1)
    assert add_qs([q4, q5]) == create_q(1, 1)
    assert add_qs([q1, q2, q3, q4, q5]) == create_q(13, 6)


def to_str(q):
    if get_den(q) == 1:
        return str(get_num(q))
    return str(get_num(q)) + "/" + str(get_den(q))
