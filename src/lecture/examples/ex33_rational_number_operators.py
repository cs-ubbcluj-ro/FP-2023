"""
Created on Nov 1, 2016

@author: Arthur
"""
from math import gcd


class rational:
    # Class field is shared by all instances
    number_of_instances = 0
    """
      Abstract data type rational numbers
      Domain: {a/b  where a,b integer numbers, b!=0, greatest common divisor a, b =1}
    """

    def __init__(self, a, b=1):
        """
          Initialise a rational number
          a,b int numbers
        """
        if b == 0:
            raise ValueError("Denominator cannot be 0!")

        rational.number_of_instances += 1
        d = gcd(a, b)
        self.__nominator = a // d
        self.__denominator = b // d

    def get_denominator(self):
        """
           Getter method
           return the denominator of the rational number
        """
        return self.__denominator

    def get_numerator(self):
        """"
          Getter method
          return the nominator of the method
        """
        return self.__nominator

    @staticmethod
    def get_total_number_of_instances():
        """
          Get the number of created rational number instances
          return integer
        """
        return rational.number_of_instances

    def add(self, a):
        """
        add 2 rational numbers
        a is a rational number
        Return the sum of two rational numbers as an instance of rational number.
        Raise ValueError if the denominators are zero.
        """
        if self.get_denominator() == 0 or a.get_denominator() == 0:
            raise ValueError("0 denominator not allowed")
        return rational(self.get_numerator() * a.get_denominator() + self.get_denominator() * a.get_numerator(),
                        self.get_denominator() * a.get_denominator())

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
        return float(self.get_numerator()) / self.get_denominator()

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
        return str(self.__nominator) + "/" + str(self.__denominator)

    def __eq__(self, other):
        """
          Verify if 2 rational numbers are equals
          other - a rational number
          return True if the instance is equal with other
        """
        return self.__nominator == other.__nominator and self.__denominator == other.__denominator


def test_rational_add():
    r1 = rational(1, 2)
    r2 = rational(1, 3)
    r3 = r1.add(r2)
    assert r3.get_numerator() == 5
    assert r3.get_denominator() == 6
    assert r3 == rational(5, 6)


def test_equal():
    """
      test function for testing == for 2 rational numbers
    """
    r1 = rational(1, 3)
    assert r1 == r1
    r2 = rational(1, 3)
    assert r1 == r2
    r1 = rational(1, 3)
    r1 = r1.add(rational(2, 3))
    r2 = rational(1, 1)
    assert r1 == r2


def test_compare_operator():
    """
    Test function for < >
    """
    r1 = rational(1, 3)
    r2 = rational(2, 3)
    assert r2 > r1
    assert r1 < r2


def test_add_operator():
    """
      Test function for the + operator
    """
    r1 = rational(1, 3)
    r2 = rational(1, 3)
    r3 = r1 + r2
    assert r3 == rational(2, 3)


def test_create():
    """
      Test function for creating rational numbers
    """
    r1 = rational(1, 3)  # create the rational number 1/3
    assert r1.get_numerator() == 1
    assert r1.get_denominator() == 3
    r1 = rational(4, 3)  # create the rational number 4/3
    assert r1.get_numerator() == 4
    assert r1.get_denominator() == 3


if __name__ == "__main__":
    test_create()
    test_equal()
    test_rational_add()
    test_add_operator()
    test_compare_operator()

    '''
        How many actual rational numbers have we created?
    '''
    print("Total numer of instances ", rational.get_total_number_of_instances())
