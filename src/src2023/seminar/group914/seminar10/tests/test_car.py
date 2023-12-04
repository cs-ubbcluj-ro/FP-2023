from unittest import TestCase

from src2023.seminar.group914.seminar10.domain.car import Car


class TestCar(TestCase):
    """
    class TestCar inherits from class TestCase
        -> all methods and non-private fields in TestCase can be accesed by the
           inheriting class

    unittest.TestCase is the base unit testing class in PyUnit
        -> all classes that inherit from TestCase are test classes
    """

    def setUp(self):
        """
        runs before all test_ methods
        :return:
        """
        self.__c = Car("CJ 01 ABC", "Toyota", "Yaris", "red")

    def tearDown(self):
        """
        runs after all tests are complete
        :return:
        """

    def test_car_1(self):
        # not nice, because AssertionError stops all tests from running
        assert self.__c.licence_plate == "not the correct plates!"

        self.assertEqual(self.__c.licence_plate, "CJ 01 ABC", "oopsie!")

    def test_car_2(self):
        c = Car("CJ 01 ABC", "Toyota", "Yaris", "red")

        # not nice, because AssertionError stops all tests from running
        # assert self.__c.licence_plate == "CJ 01 ABC"

        self.assertEqual(self.__c.licence_plate, "CJ 01 ABC", "oopsie!")

    def test_car_3(self):
        c = Car("CJ 01 ABC", "Toyota", "Yaris", "red")

        # not nice, because AssertionError stops all tests from running
        assert c.licence_plate == "CJ 01 ABC"

        self.assertEqual(self.__c.licence_plate, "CJ 01 ABC", "oopsie!")


class TestClassTwo(TestCase):
    def setUp(self):
        """
        runs before all test_ methods
        :return:
        """
        self.__c = Car("CJ 01 ABC", "Toyota", "Yaris", "red")

    def test_one(self):
        c = Car("CJ 01 ABC", "Toyota", "Yaris", "red")

        # not nice, because AssertionError stops all tests from running
        assert c.licence_plate == "CJ 01 ABC"

        self.assertEqual(self.__c.licence_plate, "CJ 01 ABC", "oopsie!")
