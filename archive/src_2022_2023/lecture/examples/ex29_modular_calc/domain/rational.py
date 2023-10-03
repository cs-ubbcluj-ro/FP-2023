"""
  Utility module to work with rational numbers
"""
from math import gcd


def create_rational(nom, den=1):
    if den == 0:
        raise ValueError("Denominator cannot be 0")
    d = gcd(nom, den)
    return [nom // d, den // d]


def get_numerator(q):
    return q[0]


def get_denominator(q):
    return q[1]


def add(q1, q2):
    """
    Return the sum of two rational numbers.
    q1, q2 the rational numbers
    return the sum
    """
    return create_rational(get_numerator(q1) * get_denominator(q2) + get_numerator(q2) * get_denominator(q1), get_denominator(q1) * get_denominator(q2))


def test_add():
    """
      Test function for rational_add
    """
    assert add(create_rational(1, 2), create_rational(1, 3)) == create_rational(5, 6)
    assert add(create_rational(1, 2), create_rational(1, 2)) == create_rational(1)
