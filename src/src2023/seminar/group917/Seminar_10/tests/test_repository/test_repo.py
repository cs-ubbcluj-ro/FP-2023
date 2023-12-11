import unittest

from src2023.seminar.group917.Seminar_10.domain.person import Person
from src2023.seminar.group917.Seminar_10.repository.person_repository import PersonFileRepository
from src2023.seminar.group917.Seminar_10.repository.repo_exceptions import RepositoryException, \
    PersonDoesNotExistException
from src2023.seminar.group917.Seminar_10.utils.file_utils import clear_file_content


class TestRepoFile(unittest.TestCase):
    def setUp(self):
        #Method is run before each test
        print("Called setUp.")
        clear_file_content('test_persons.txt')
        self._test_repo = PersonFileRepository("test_persons.txt")

    def test_store(self):

        person = Person('1730523123456', 'Marcel')
        self._test_repo.store(person)
        self.assertEqual(self._test_repo.size, 1)
        self.assertRaises(RepositoryException, self._test_repo.store, person)

        # try:
        #     self._test_repo.store(person)
        #     assert False
        # except RepositoryException:
        #     assert True

        person2 = Person('1710523123456', 'Marcel')
        self._test_repo.store(person2)
        self.assertEqual(self._test_repo.size, 2)

    def test_find(self):

        self.assertEqual(self._test_repo.size, 0)

        person1 = Person('1910918123456', "Mircea")
        person2 = Person('2920918123456', "Carina")
        person3 = Person('5930918123456', "Alex")

        self._test_repo.store(person1)
        self._test_repo.store(person2)
        self._test_repo.store(person3)

        self.assertEqual(self._test_repo.size, 3)

        self.assertIsNotNone(self._test_repo.get('1910918123456'))
        self.assertIsNotNone(self._test_repo.get('2920918123456'))
        self.assertIsNotNone(self._test_repo.get('5930918123456'))
        self.assertRaises(PersonDoesNotExistException,self._test_repo.get,'6931118123456')

    def test_delete(self):

        person1 = Person('1910918123456', "Mircea")
        person2 = Person('2920918123456', "Carina")
        person3 = Person('5930918123456', "Alex")

        self._test_repo.store(person1)
        self._test_repo.store(person2)
        self._test_repo.store(person3)
        self.assertEqual(self._test_repo.size, 3)

        deleted_person = self._test_repo.delete('1910918123456')
        self.assertEqual(self._test_repo.size, 2)
        self.assertRaises(PersonDoesNotExistException,self._test_repo.get,'1910918123456')
        self.assertEqual(deleted_person.name, "Mircea")

        deleted_person = self._test_repo.delete('5930918123456')
        self.assertEqual(self._test_repo.size, 1)
        self.assertRaises(PersonDoesNotExistException,self._test_repo.get,'5930918123456')
        self.assertEqual(deleted_person.name, "Alex")

        self._test_repo.store(Person('5930918123456', 'Alexis'))
        self.assertEqual(self._test_repo.size, 2)

        deleted_person = self._test_repo.delete('5930918123456')
        self.assertEqual(self._test_repo.size, 1)
        self.assertRaises(PersonDoesNotExistException,self._test_repo.get,'5930918123456')
        self.assertEqual(deleted_person.name, "Alexis")
        self.assertRaises(RepositoryException, self._test_repo.delete, '5930918123451')

    def tearDown(self):
        print("Called tearDown.")
        clear_file_content('test_persons.txt')
