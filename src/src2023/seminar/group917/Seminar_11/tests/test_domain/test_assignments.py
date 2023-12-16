import unittest

from domain.assignment import Assignment
from domain.person import Person
from domain.task import Task


class AssignmentTests(unittest.TestCase):
    def test_create_assignment(self):
        task = Task(1, 'Decorate for Christmas', 18, 12, 'pending')
        person = Person('2980107123456', 'Alessia')

        assignment = Assignment(1, task, person, 9.3)

        assert (assignment.task == task)
        assert (assignment.person == person)
        assert (assignment.evaluation == 9.3)

    def test_equality(self):
        pass

    def test_validate_assignment(self):
        pass
