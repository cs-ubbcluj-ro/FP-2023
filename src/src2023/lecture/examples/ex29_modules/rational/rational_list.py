"""
Docstring for Rational number represented using a list

Created on Oct 21, 2018
@author: Arthur
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
