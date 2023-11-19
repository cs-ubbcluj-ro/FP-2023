"""
Rational number represented as a list
"""
from math import gcd


def create_q(num: int = 0, den: int = 1):
    """
    Return rational number
    :param num: Numerator
    :param den: Denominator, den != 0
    :return: The number represented as a list
    raise ValueError if den == 0
    """
    if den == 0:
        raise ValueError("Denominator cannot be 0")
    g = gcd(num, den)

    return [num // g, den // g]


def get_den(q) -> int:
    return q[1]


def get_num(q) -> int:
    return q[0]

if __name__ == "__main__":
    print("In rational number module")
    print(dir())