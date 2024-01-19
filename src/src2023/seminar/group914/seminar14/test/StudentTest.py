from unittest import TestCase

from src2023.seminar.group914.seminar14.domain.student import Student


class StudentTest(TestCase):

    def test_student(self):
        s = Student(1000, "Popescu Aurel", "321")
        self.assertEqual(s.id, 1000)
        self.assertEqual(s.group, "321")
