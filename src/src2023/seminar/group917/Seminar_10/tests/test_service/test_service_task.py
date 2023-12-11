import unittest

from src2023.seminar.group917.Seminar_10.domain.validators import TaskValidator
from src2023.seminar.group917.Seminar_10.repository.repo_exceptions import RepositoryException
from src2023.seminar.group917.Seminar_10.repository.task_repository import TaskInMemoryRepository
from src2023.seminar.group917.Seminar_10.service.task_service import TaskController


class TaskServiceTests(unittest.TestCase):
    def setUp(self):
        repo = TaskInMemoryRepository()
        validator = TaskValidator()
        self._task_service = TaskController(repo, validator)
        self._task_service.add_task(1, "Travel to see Grand Canyon", 11, 9, 'pending')
        self._task_service.add_task(2, "Travel abroad", 10, 5, 'pending')
        self._task_service.add_task(3, "Try new banana bread recipe", 11, 2, "done")
        self._task_service.add_task(4, "Host a Halloween party", 31, 10, 'in-progress')
        self._task_service.add_task(5, "Buy stuff for New Year party", 28, 12, "pending")
        self._task_service.add_task(6, "Decorate the house for New Year party", 28, 12, "pending")
        self._task_service.add_task(7, "Find costume for Halloween", 31, 10, "pending")
        self._task_service.add_task(8, "Decorate garden for Halloween", 31, 10, "pending")


    def test_add(self):
        self._task_service.add_task(10, "Visit Hawaii", 10, 5, 'pending')
        self.assertEqual(len(self._task_service.get_all_tasks()),9)
        self.assertRaises(RepositoryException, self._task_service.add_task,10, "Visit Hawaii", 10, 5, 'pending')


    def test_delete(self):
        pass

    def test_filter_by_description(self):

        filtered_by_travel = self._task_service.filter_by_description('travel')
        assert (len(filtered_by_travel) == 2)
        assert (len(self._task_service.get_all_tasks()) == 8)

        filtered_by_recipe = self._task_service.filter_by_description('recipe')
        assert (len(filtered_by_recipe) == 1)
        assert (len(self._task_service.get_all_tasks()) == 8)

        filtered_by_cook = self._task_service.filter_by_description('cook')
        assert (len(filtered_by_cook) == 0)
        assert (len(self._task_service.get_all_tasks()) == 8)

    def test_get_report_by_day(self):

        report_dict = self._task_service.get_report_by_day()
        assert (len(report_dict['28/12']) == 2)

        assert (len(report_dict['31/10']) == 3)

        assert (len(report_dict['10/5']) == 1)

        try:
            number_of_tasks = len(report_dict['1-1'])
            assert False
        except KeyError:
            assert True
