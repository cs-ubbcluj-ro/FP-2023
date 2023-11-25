"""
What is a class?
    - a type = domain + operations

What does this help with?
    -> encapsulation (put data and its operations
    together)
    -> information hiding (abstraction)

"""


class RationalError(Exception):
    """
    We define type RationalError, an exception
    RationalError is a subclass of Exception, so that
    we can use it in try ... except blocks
    """
    pass


class Rational(object):
    """
    class Rational is a subclass of object
    object is the root of the class hierarchy
    """
    __object_count = 0

    def __init__(self, num: int = 0, den: int = 1):
        # num -> public, accessible from outside class
        # self.num = num

        # _num -> protected, should not be accessed
        # from outside class
        # self._num = num

        # __num -> private, it cannot be accessed
        # from outside class
        if den == 0:
            raise RationalError()
        self.__num = num
        self.__den = den
        Rational.__object_count += 1

    @staticmethod
    def get_object_count():
        """
        self cannot be used in static methods
        """
        return Rational.__object_count

    def get_num(self):
        # __num is visible as we are inside the class
        return self.__num

    def get_den(self):
        return self.__den

    def __add(self, q):
        """
        self + q => returns a new instance of Rational
        :param q:
        :return:
        """
        num = self.get_num() * q.get_den() + q.get_num() * self.get_den()
        den = self.get_den() * q.get_den()
        return Rational(num, den)

    def __add__(self, other):
        return self.__add(other)

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)


q1 = Rational(1, 2)  # 1/2
print(str(q1))

# print(q1.__num)
# q1.test_field = "abcde"
# print(q1._Rational__den)
# print(dir(q1))

# maybe we want to prevent what happens below
# q1.num = "abcd"
# q1.den = 0


q2 = Rational(3)  # 3
q3 = Rational()  # 0

# q =
# print(q1.add(q2).add(q2).add(q2))

# q1.add(q2)
# Rational.add is called, self is played by q1
# q is played by q2
# print(Rational.add(q1, q2))

print(q1 + q2 + q2 + q2)

print(Rational.get_object_count())

# print(q1.test_field)
# print(q2.test_field)

# print(dir(q2))
# Rational(0,0)
