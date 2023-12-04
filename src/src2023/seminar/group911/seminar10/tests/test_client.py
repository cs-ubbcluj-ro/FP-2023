from unittest import TestCase

from src2023.seminar.group911.seminar10.domain.client import Client


class TestClient(TestCase):
    def test_init(self):
        # self.assertRaises(ValueError, Client.__init__, 1234, "nume")
        with self.assertRaises(ValueError) as cm:
            c = Client(1234, "nume")

    def test_id(self):
        c = Client("id", "nume")
        self.assertEqual(c.id, "id")

    def test_name(self):
        c = Client("id", "nume")
        self.assertEqual(c.name, "nume")

    def test_eq(self):
        c = Client("id", "nume")
        self.assertNotEqual(c, "id nume")
