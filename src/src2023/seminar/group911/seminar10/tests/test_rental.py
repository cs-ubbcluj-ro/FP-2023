from datetime import date
from unittest import TestCase

from src2023.seminar.group911.seminar10.domain.car import Car
from src2023.seminar.group911.seminar10.domain.client import Client
from src2023.seminar.group911.seminar10.domain.rental import Rental


class TestRental(TestCase):

    def setUp(self):
        """
        Executed only once
        Runs before any of the test_ functions
        Used to set up the test suite
        """
        self.__client = Client("id", "nume")
        self.__car = Car("BH 00 KYS", "Aro", "240", "Gray")

    def tearDown(self):
        """
        Executed only once
        Final method that runs
        Opposite of setUp
        """
        pass

    def test_id(self):
        c = Rental("id", self.__car, self.__client, date.today(), date.today())
        self.assertEqual(c.id, "id")

    def test_car(self):
        c = Rental("id", Car("BH 00 KYS", "Aro", "240", "Gray"), Client("id", "nume"), date.today(),
                   date.today())
        self.assertEqual(c.car, Car("BH 00 KYS", "Aro", "240", "Gray"))

    def test_client(self):
        c = Rental("id", Car("BH 00 KYS", "Aro", "240", "Gray"), Client("id", "nume"), date.today(),
                   date.today())
        self.assertEqual(c.client, Client("id", "nume"))

    def test_start(self):
        c = Rental("id", Car("BH 00 KYS", "Aro", "240", "Gray"), Client("id", "nume"), date.today(),
                   date.today())
        self.assertEqual(c.start, date.today())

    def test_end(self):
        c = Rental("id", Car("BH 00 KYS", "Aro", "240", "Gray"), Client("id", "nume"), date.today(),
                   date.today())
        self.assertEqual(c.end, date.today())
