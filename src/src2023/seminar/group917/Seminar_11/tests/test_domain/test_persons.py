import unittest

from domain.person import Person


class PersonTests(unittest.TestCase):
    # https://docs.python.org/3/library/unittest.html
    def test_creation(self):
        person = Person('6050706437566', 'Alessia')
        self.assertEqual(person.name, 'Alessia')
        self.assertEqual(person.cnp, '6050706437566')
        self.assertEqual(person.birth_day, 6)
        self.assertEqual(person.birth_month, 7)
        self.assertEqual(person.birth_year, 2005)

        person = Person('1991002122222', 'Daniel')
        self.assertEqual(person.name, 'Daniel')
        self.assertEqual(person.cnp, '1991002122222')
        self.assertEqual(person.birth_day, 2)
        self.assertEqual(person.birth_month, 10)
        self.assertEqual(person.birth_year, 1999)

    def test_equality(self):
        person1 = Person('6050706437566', 'Alessia')
        person2 = Person('6050706437566', 'Sandra')
        self.assertEqual(person1, person2)

        person1 = Person('6050706437566', 'Alessia')
        person2 = Person('2940706437566', 'Alessia')
        self.assertNotEqual(person1, person2)

    # TO-DO: test validate person


if __name__ =='__main__':
    unittest.main()
