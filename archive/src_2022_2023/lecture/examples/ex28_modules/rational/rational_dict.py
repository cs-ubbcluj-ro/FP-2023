"""
Docstring for Rational number represented using a dict

Created on Oct 21, 2018
@author: Arthur
"""
import math


def create_rational(nom, den=1):
    if den == 0:
        raise ValueError("Denominator cannot be 0")

    d = math.gcd(nom, den)
    return {"nom": nom // d, "denom": den // d}


def get_numerator(q):
    return q["nom"]


def get_denominator(q):
    return q["denom"]
