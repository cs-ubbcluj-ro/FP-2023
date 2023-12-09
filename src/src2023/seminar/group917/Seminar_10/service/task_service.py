from src2023.seminar.group917.Seminar_10.domain.task import Task


class TaskController:
    def __init__(self, repository, task_validator):
        self.__task_validator = task_validator
        self.__repo = repository

    def add_task(self, task_id, description: str, day: int, month: int, status: str) -> None:
        """
        Add task 
        :raises: TaskValidationException if task is invalid
                 RepositoryException if there already is a task with the given id
        """

        task = Task(task_id, description, day, month, status)
        self.__task_validator.validate(task)
        self.__repo.store(task)

    def delete_task(self, task_id: int):
        """
        Delete task with given id
        :raises: Repository exception if a task with given id doesn't exist
        """
        return self.__repo.delete(task_id)


    def filter_by_description(self, description: str) -> list:
        """
        Return a list of tasks which have the given description in their description (as substring)

        """
        return [task for task in self.__repo.get_all() if description.lower() in task.description.lower()]

    def get_report_by_day(self) -> dict:
        """
        Create report of tasks by dd/mm date

        """
        #Extra-reading: defaultdict
        day_dictionary = {}
        for task in self.__repo.get_all():
            if task.complete_date in day_dictionary:
                day_dictionary[task.complete_date].append(task)
            else:
                day_dictionary[task.complete_date] = [task]
        return day_dictionary

    def get_all_tasks(self) -> list:

        return self.__repo.get_all()

