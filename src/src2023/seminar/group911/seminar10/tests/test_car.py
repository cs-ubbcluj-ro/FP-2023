from unittest import TestCase

from src2023.seminar.group911.seminar10.domain.car import Car


class TestCar(TestCase):
    """
    class TestCar is inherited from class TestCase
    class TestCar has all fields, properties and
    methods of class TestCase
    """

    def test_car_license(self):
        c = Car("CJ 01 TYU", "Mazda", "3", "red")
        """
        How does assert work?
        condition true => code keeps running
        condition false => AssertionError raised, and
            program crash
        """
        # assert c.license_plate == "CJ 01 TYU"
        """
        The one below does not crash the program
        """
        self.assertEqual(c.license_plate, "CJ 01 TYU")
        # TestCase.assertEqual()

    def test_car_make(self):
        c = Car("CJ 01 TYU", "Mazda", "3", "red")
        self.assertEqual(c.make, "Mazda")
        self.assertEqual(c.make, "Toyota")

    def test_car_color(self):
        c = Car("CJ 01 TYU", "Mazda", "3", "red")
        self.assertEqual(c.color, "red")
        c.color = "blue"
        self.assertEqual(c.color, "blue")