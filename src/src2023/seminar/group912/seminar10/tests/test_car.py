from unittest import TestCase

from src2023.seminar.group912.seminar10.domain.car import Car


class TestCar(TestCase):
    """
    class TestCar is a subclass of TestCase
        => every non-private data member, property and method of TestCase are available in TestCar
        => TestCar "is a" TestCase
    """

    def test_car_license(self):
        c = Car("CJ 09 TGV", "Dacia", "Jogger", "orange")
        """
        How assert works
        1. If condition is true => nothing happens
        2. If condition is false => AssertionError, program crash 
        """
        # assert c.licence_plate == "CJ 09 TGV"
        self.assertEqual(c.licence_plate, "CJ 09 TGV")

    def test_car_make(self):
        c = Car("CJ 09 TGV", "Dacia", "Jogger", "orange")
        self.assertEqual(c.make, "Dacia")
        self.assertEqual(c.make, "Mazda")

    def test_car_eq(self):
        c0 = Car("CJ 09 TGV", "Dacia", "Jogger", "orange")
        c1 = Car("CJ 09 TGV", "Dacia", "Jogger", "orange")
        self.assertEqual(c0, c1)
        c1 = Car("CJ 09 UYT", "Dacia", "Jogger", "orange")
        self.assertNotEqual(c0, c1)
        self.assertNotEqual(c0, "CJ 09 TGV")
