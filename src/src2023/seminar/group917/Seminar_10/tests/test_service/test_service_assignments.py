import unittest

from src2023.seminar.group917.Seminar_10.domain.domain_exceptions import AssignmentValidationException
from src2023.seminar.group917.Seminar_10.domain.validators import AssignmentValidator
from src2023.seminar.group917.Seminar_10.repository.assignment_repository import AssignmentInMemoryRepository
from src2023.seminar.group917.Seminar_10.repository.person_repository import PersonFileRepository
from src2023.seminar.group917.Seminar_10.repository.repo_exceptions import AssignmentAlreadyExistsException, \
    PersonDoesNotExistException, RepositoryException
from src2023.seminar.group917.Seminar_10.repository.task_repository import TaskFileRepository
from src2023.seminar.group917.Seminar_10.service.assignment_service import AssignmentService
from src2023.seminar.group917.Seminar_10.utils.file_utils import clear_file_content, copy_file_content


class AssignmentServiceTests(unittest.TestCase):
    def setUp(self):
        clear_file_content('test_tasks.txt')
        copy_file_content('default_tasks.txt', 'test_tasks.txt')
        task_repo = TaskFileRepository('test_tasks.txt')

        clear_file_content('test_persons.txt')
        copy_file_content('default_persons.txt', 'test_persons.txt')
        person_repo = PersonFileRepository('test_persons.txt')

        assignment_repo = AssignmentInMemoryRepository()
        assignment_validator = AssignmentValidator()
        self._assignment_service = AssignmentService(task_repo, person_repo, assignment_repo, assignment_validator)
    def test_add_assignment(self):
      
        # all ok, can add
        self._assignment_service.create_assignment(1, 1, '6050706437566', 7)
        self.assertEqual(len(self._assignment_service.get_all()),1)
    
        self._assignment_service.create_assignment(2, 1, '1760920213245', 7)
        self.assertEqual(len(self._assignment_service.get_all()),2)


        self.assertRaises(AssignmentAlreadyExistsException, self._assignment_service.create_assignment, 2, 1, '1760920213245', 7)
        self.assertRaises(PersonDoesNotExistException, self._assignment_service.create_assignment, 3, 1, '1760920213241', 5)
        self.assertRaises(RepositoryException, self._assignment_service.create_assignment, 4, 1352, '6050706437566', 5)
        self.assertRaises(AssignmentValidationException, self._assignment_service.create_assignment, 5, 1, '6050706437566', 100)

    


