from unittest import TestCase

from src2023.seminar.group913.seminar10.domain.car import Car


class TestCar(TestCase):
    """
    Class TestCar inherits from class TestCase, we say TestCar "is a" TestCase
        inherits -> TestCar class has the non-private fields, methods, properties of
                    TestCase
                 -> helps with reusing code
                 -> tells PyCharm that TestCar is a test class
    """

    def setUp(self):
        """
        setUp - runs before any of the test_ methods
        :return:
        """
        self.__c = Car("CJ 09 ERT", "Toyota", "Corolla", "blue")

    def tearDown(self):
        """
        Opposite of setUp (close files, DB connections, etc.)
        :return:
        """
        pass

    def test_car_license_plate(self):
        # c = Car("CJ 09 ERT", "Toyota", "Corolla", "blue")

        """
        How does assert behave?
            condition true  => nothing happens (test has passed)
            condition false => AssertionError, program crash (test has failed) 
        """
        # assert c.license_plate == "CJ 09 ERT"

        """
        I want assert to tell me the test failed without crashing the program
        """
        self.assertEqual(self.__c.license_plate, "CJ 09 ERT")

    def test_car_license_make(self):
        # c = Car("CJ 09 ERT", "Toyota", "Corolla", "blue")
        self.assertEqual(self.__c.make, "Toyota")
        self.assertEqual(self.__c.make, "Mazda")

    def test_car_colo(self):
        # c = Car("CJ 09 ERT", "Toyota", "Corolla", "blue")
        self.assertEqual(self.__c.color, "blue")
        self.__c.color = "red"
        self.assertEqual(self.__c.color, "red")
