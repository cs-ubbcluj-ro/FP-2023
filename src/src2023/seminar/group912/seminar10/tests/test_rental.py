# Ciupe Marius Daniel
from datetime import date
from unittest import TestCase

from src2023.seminar.group912.seminar10.domain.car import Car
from src2023.seminar.group912.seminar10.domain.client import Client
from src2023.seminar.group912.seminar10.domain.rental import Rental


class TestRental(TestCase):
    def testCase(self):
        a = Rental(100, Car('CJ 69 XXX', 'NuStiu', 'FaraPermis', 'cyan'),
                   Client(5000, 'Juan'), date(2000, 12, 10), date(2001, 1, 10))

        b = Rental(300, Car('CJ 13 COC', 'Masina', 'Urasc', 'pink'),
                   Client(4000, 'Escobar'), date(2000, 10, 10), date(2000, 10, 15))

        self.assertEquals(len(b), 5)
        self.assertEquals(len(a), 31)

        c = Rental('0', Car('CJ 23 KOF', 'Masina', 'Frumi', 'MergeBine', 'orange'), )

        pass
