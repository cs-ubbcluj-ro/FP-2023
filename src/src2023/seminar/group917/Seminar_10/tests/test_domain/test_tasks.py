import unittest

from src2023.seminar.group917.Seminar_10.domain.domain_exceptions import TaskValidationException
from src2023.seminar.group917.Seminar_10.domain.task import Task
from src2023.seminar.group917.Seminar_10.domain.validators import TaskValidator


class TaskTests(unittest.TestCase):
    def setUp(self):
        self._task_validator = TaskValidator()

    def test_create_task(self):
        pass

    def test_equality(self):
        pass

    def test_validate_task(self):
        task1 = Task(1, "Host Movie Marathon", 10, 9, 'pending')
        self.assertIsNone(self._task_validator.validate(task1))

        task2 = Task(2, "H", 10, 9, 'pending')
        self.assertRaises(TaskValidationException, self._task_validator.validate, task2)

        task3 = Task(1, "Movie Marathon", 56, 8, 'pending')
        self.assertRaises(TaskValidationException, self._task_validator.validate, task3)

        task4 = Task(1, "Host movie marathon", 10, 91, 'pending')
        self.assertRaises(TaskValidationException, self._task_validator.validate, task4)

        task5 = Task(1, "Host movie marathon", 10, 9, 'something')
        self.assertRaises(TaskValidationException, self._task_validator.validate, task5)
