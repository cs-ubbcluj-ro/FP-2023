from src2023.seminar.group917.Seminar_10.domain.task import Task
from src2023.seminar.group917.Seminar_10.repository.repo_exceptions import RepositoryException


class TaskInMemoryRepository:
    def __init__(self):
        self.__tasks = {}

    def store(self, task):
        """
        Add a given task
        :raises: RepositoryException if task already exists
        """

        if task.id in self.__tasks:
            raise RepositoryException("There is already a task with this ID.")
        self.__tasks[task.id] = task

    def get(self, task_id):
        """
        Find task with given id
        """
        try:
            return self.__tasks[task_id]
        except KeyError:
            raise RepositoryException("No task with this ID exists.")

    def delete(self, task_id):
        """
        Remove task with given ID
        :raises: RepositoryException if task does not exist
        """
        try:
            task_to_delete = self.__tasks[task_id]
            del self.__tasks[task_id]
            return task_to_delete
        except KeyError:
            raise RepositoryException("No task with this ID exists.")

    def get_all(self) -> list:

        return list(self.__tasks.values())

    def size(self):
        return len(self.__tasks)


class TaskFileRepository:
    """
    Repository which handles data from file. Does not use inheritance. Uses list to hold tasks
    """

    def __init__(self, filename):
        self.__filename = filename

    def _read_from_file(self):
        f = open(self.__filename, mode='r')

        tasks = []
        lines = f.readlines()
        for line in lines:
            elements = line.split(',')
            elements = [element.strip() for element in elements]
            id = int(elements[0])
            description = elements[1]
            day = int(elements[2])
            month = int(elements[3])
            status = elements[4]
            task = Task(id, description, day, month, status)
            tasks.append(task)
        f.close()
        return tasks

    def _write_to_file(self, task_list):
        with open(self.__filename, mode='w') as f:
            for task in task_list:
                task_elements = [task.id, task.description, task.deadline_day, task.deadline_month,
                                 task.status]
                task_elements = [str(element) for element in task_elements]
                line = ', '.join(task_elements) + '\n'
                f.write(line)

    def store(self, task):
        tasks = self._read_from_file()

        if task in tasks:
            raise RepositoryException("There is already a task with this ID.")

        tasks.append(task)
        self._write_to_file(tasks)

    def get(self, task_id):
        tasks = self._read_from_file()
        for task in tasks:
            if task.id == task_id:
                return task
        raise RepositoryException("No task with this ID exists.")

    def delete(self, id):

        tasks = self._read_from_file()

        task_to_delete = self.get(id)
        tasks.remove(task_to_delete)
        self._write_to_file(tasks)
        return task_to_delete


    def get_all(self) -> list:
        return self._read_from_file()
    
    
    def size(self):
        return len(self._read_from_file())
