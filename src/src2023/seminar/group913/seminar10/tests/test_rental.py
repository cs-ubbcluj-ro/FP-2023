from datetime import date
from unittest import TestCase

from src2023.seminar.group913.seminar10.domain.car import Car
from src2023.seminar.group913.seminar10.domain.client import Client
from src2023.seminar.group913.seminar10.domain.rental import Rental


class RentalTests(TestCase):
    def test_rental_constructor(self):
        client = Client("1", "John")
        car = Car("1", "Ford", "Focus", "Red")
        start = date(2021, 1, 1)
        end = date(2021, 1, 2)

        rental = Rental("1", client, car, start, end)

        self.assertEqual(rental.id, "1")
        self.assertEqual(rental.client, client)
        self.assertEqual(rental.car, car)
        self.assertEqual(rental.start, start)
        self.assertEqual(rental.end, end)

    def test_rental_constructor_invalid_client(self):
        car = Car("1", "Ford", "Focus", "Red")
        start = date(2021, 1, 1)
        end = date(2021, 1, 2)

        with self.assertRaises(TypeError):
            Rental("1", 1, car, start, end)

    def test_rental_constructor_invalid_car(self):
        client = Client("1", "John")
        start = date(2021, 1, 1)
        end = date(2021, 1, 2)

        with self.assertRaises(TypeError):
            Rental("1", client, 1, start, end)

    def test_rental_constructor_invalid_start(self):
        client = Client("1", "John")
        car = Car("1", "Ford", "Focus", "Red")
        end = date(2021, 1, 2)

        with self.assertRaises(TypeError):
            Rental("1", client, car, 1, end)

    def test_rental_eq(self):
        client = Client("1", "John")
        car = Car("1", "Ford", "Focus", "Red")
        start = date(2021, 1, 1)
        end = date(2021, 1, 2)

        rental1 = Rental("1", client, car, start, end)
        rental2 = Rental("1", client, car, start, end)

        self.assertEqual(rental1, rental2)
