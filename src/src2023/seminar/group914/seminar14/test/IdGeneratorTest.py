from unittest import TestCase
import os

from src2023.seminar.group914.seminar14.services.idgenerator import IdGenerator


class IdGeneratorTest(TestCase):
    # don't hardcode file names in the program
    test_file_name = "test_idgen.txt"

    def test_idgenerator(self):
        idgen = IdGenerator(IdGeneratorTest.test_file_name)
        self.assertEqual(idgen.generate_id(), 1)
        self.assertEqual(idgen.generate_id(), 2)
        self.assertEqual(idgen.generate_id(), 3)

    def tearDown(self):
        if os.path.exists(IdGeneratorTest.test_file_name):
            os.remove(IdGeneratorTest.test_file_name)
