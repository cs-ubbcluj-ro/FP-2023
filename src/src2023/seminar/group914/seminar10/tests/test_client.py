from unittest import TestCase

from src2023.seminar.group914.seminar10.domain.client import Client


class TestClient(TestCase):
    def test_client_1(self):
        c = Client("100", "Ana")
        self.assertEqual(c.name, "Ana", "oopsie!")

    def test_client_2(self):
        c = Client("100", "Ana")
        self.assertEqual(c.id, "100", "oopsie!")

    def test_client_3(self):
        c = Client("100", "Ana")
        self.assertEqual(c.id, "1000", "oopsie client!")

    def test_client_eq(self):
        c = Client("100", "Ana")
        c1 = Client("100", "Banana")

        self.assertEqual(c, c1)
        self.assertNotEqual(c1, "banana")
