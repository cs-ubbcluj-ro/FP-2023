"""
Created on Nov 1, 2016

@author: Arthur
"""
from math import gcd


class rational:
    """
      Abstract data type rational number
      Domain: {a/b  where a,b integer numbers, b!=0, greatest common divisor a, b =1}
    """

    def __init__(self, a, b=1):
        """
          Initialise a rational number
          a,b integer numbers
        """
        if b == 0:
            raise ValueError("Denominator cannot be 0!")

        d = gcd(a, b)
        self.__nominator = a // d
        self.__denominator = b // d

    def get_numerator(self):
        """
           Getter method
           return the denominator of the rational number
        """
        return self.__denominator

    def get_denominator(self):
        """"
          Getter method
          return the nominator of the method
        """
        return self.__nominator

    def add(self, a):
        """
        add 2 rational numbers
        a is a rational number
        Return the sum of two rational numbers as an instance of rational number.
        Raise ValueError if the denominators are zero.
        """
        return rational(self.get_denominator() * a.get_numerator() + self.get_numerator() * a.get_denominator(),
                        self.get_numerator() * a.get_numerator())


def test_rational_add():
    r1 = rational(1, 2)
    r2 = rational(1, 3)
    r3 = r1.add(r2)
    assert r3.get_denominator() == 5
    assert r3.get_numerator() == 6


def test_create():
    r1 = rational(1, 3)  # create the rational number 1/3
    assert r1.get_denominator() == 1
    assert r1.get_numerator() == 3
    r1 = rational(4, 3)  # create the rational number 4/3
    assert r1.get_denominator() == 4
    assert r1.get_numerator() == 3


if __name__ == "__main__":
    test_create()
    test_rational_add()
