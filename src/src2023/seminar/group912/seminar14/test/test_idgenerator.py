from unittest import TestCase
import os

from src2023.seminar.group912.seminar14.IdGenerator import IdGenerator


class TestIdGenerator(TestCase):

    def setUp(self):
        self.__file_name = "test_idgen.txt"

    def test_idgenerator(self):
        idgen = IdGenerator(self.__file_name)
        for i in range(1, 10):
            self.assertEqual(idgen.get_next_id(), i)

    def tearDown(self):
        os.remove(self.__file_name)
