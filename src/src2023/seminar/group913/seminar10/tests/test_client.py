from unittest import TestCase

from src2023.seminar.group913.seminar10.domain.client import Client


class ClientTests(TestCase):
    def test_client_constructor(self):
        client = Client("1", "John")
        self.assertEqual(client.id, "1")
        self.assertEqual(client.name, "John")

    def test_client_constructor_invalid_id(self):
        with self.assertRaises(TypeError):
            Client(1, "John")

    def test_client_constructor_invalid_name(self):
        with self.assertRaises(TypeError):
            Client("1", 1)

    def test_client_eq(self):
        client1 = Client("1", "John")
        client2 = Client("1", "John")
        self.assertEqual(client1, client2)

    def test_client_eq_invalid_type(self):
        client = Client("1", "John")
        self.assertNotEqual(client, 1)
