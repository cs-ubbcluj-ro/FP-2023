"""
Created on Oct 30, 2019

@author: Arthur
"""
from math import gcd


class Rational:
    """
      Abstract data type rational numbers
      Domain: {a/b  where a,b integer numbers, b!=0, greatest common divisor a, b =1}
    """

    # Class field is shared by all instances
    _number_of_instances = 0

    def __init__(self, numerator, denominator=1):
        """
          Initialise a rational number
          numerator, denominator integers, denominator non-zero
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be 0!")

        d = gcd(numerator, denominator)
        self.num = numerator // d
        self.denom = denominator // d
        Rational._number_of_instances += 1

    @property
    def num(self):
        return self._numerator

    @num.setter
    def num(self, value):
        self._numerator = value

    @property
    def denom(self):
        return self._denominator

    @denom.setter
    def denom(self, value):
        if value == 0:
            raise ValueError("Denominator cannot be 0!")
        self._denominator = value

    @staticmethod
    def get_total_number_of_instances():
        """
          Get the number of created rational number instances
          return integer
        """
        return Rational._number_of_instances

    def add(self, a):
        """
        add 2 rational numbers
        a is a rational number
        Return the sum of two rational numbers as an instance of rational number.
        Raise ValueError if the denominators are zero.
        """
        return Rational(self.num * a.denom + self.denom * a.num, self.denom * a.denom)

    def __add__(self, other):
        """
          Overload + operator
          other  - rational number
          return a rational number, the sum of self and other
        """
        return self.add(other)

    def get_float(self):
        """
          Get the real value for the rational number
          return a float
        """
        return float(self.num) / self.denom

    def __lt__(self, ot):
        """
          Compare 2 rational numbers (less than)
          self the current instance
          ot a rational number
          return True if self<ot, False otherwise
        """
        return self.get_float() < ot.get_float()

    def __str__(self):
        """
          provide a string representation for the rational number
          return a string
        """
        return str(self.num) + "/" + str(self.denom)

    def __eq__(self, other):
        """
          Verify if 2 rational numbers are equals
          other - a rational number
          return True if the instance is equal with other
        """
        return self.num == other.num and self.denom == other.denom


def test_rational_add():
    r1 = Rational(1, 2)
    r2 = Rational(1, 3)
    r3 = r1.add(r2)
    assert r3.num == 5
    assert r3.denom == 6
    assert r3 == Rational(5, 6)


def test_equal():
    """
      test function for testing == for 2 rational numbers
    """
    r1 = Rational(1, 3)
    assert r1 == r1
    r2 = Rational(1, 3)
    assert r1 == r2
    r1 = Rational(1, 3)
    r1 = r1.add(Rational(2, 3))
    r2 = Rational(1, 1)
    assert r1 == r2


def test_compare_operator():
    """
    Test function for < >
    """
    r1 = Rational(1, 3)
    r2 = Rational(2, 3)
    assert r2 > r1
    assert r1 < r2


def test_add_operator():
    """
      Test function for the + operator
    """
    r1 = Rational(1, 3)
    r2 = Rational(1, 3)
    r3 = r1 + r2
    assert r3 == Rational(2, 3)


def test_create():
    """
      Test function for creating rational numbers
    """
    r1 = Rational(1, 3)  # create the rational number 1/3
    assert r1.num == 1
    assert r1.denom == 3
    r1 = Rational(4, 3)  # create the rational number 4/3
    assert r1.num == 4
    assert r1.denom == 3


test_create()
test_equal()
test_rational_add()
test_add_operator()
test_compare_operator()
