# Ciupe Marius Daniel
from unittest import TestCase

from src2023.seminar.group912.seminar10.domain.client import Client


class TestClient(TestCase):
    def testClient(self):
        a = Client(100, 'Tristopher')
        b = Client(100, 'Pablito')

        with self.assertRaises(TypeError):
            c = Client('0', 'Carlito')

        with self.assertRaises(TypeError):
            d = Client(1500, 80085)

        self.assertEquals(a.id, 100)
        self.assertEquals(b.name, 'Pablito')

        self.assertTrue(a == b)
        self.assertEquals(str(a), 'ID: 100; Name: Tristopher')
