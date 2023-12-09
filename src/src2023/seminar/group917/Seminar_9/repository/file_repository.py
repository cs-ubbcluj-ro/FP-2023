import pickle

from src2023.seminar.group917.Seminar_9.exceptions.exceptions import RepositoryError, DuplicateIDException


class TaskFileRepository:
    def __init__(self, filename):
        self.__filename = filename
        self.__data = {}
        try:
            self.__load_from_file()
        except FileNotFoundError:
            print("Oopsie!")
        except OSError:
            raise RepositoryError("Something went horribly wrong.")

    def __load_from_file(self):
        f = open(self.__filename, 'rb')
        self.__data = pickle.load(f)
        f.close()

    def __save_to_file(self):
        f = open(self.__filename, 'wb')
        pickle.dump(self.__data, f)
        f.close()

    def store(self, task):
        """
        Adauga un task in lista de task-uri
        :param task: task-ul de adaugat
        :type task: Task
        :return: -; lista de task-uri se modifica prin adaugarea la sfarsit a task-ului dat
        :rtype: -;
        :raises: ValueError daca exista deja task cu id-ul dat
        """

        if task.get_id() in self.__data:
            raise DuplicateIDException()
        self.__data[task.get_id()] = task
        self.__save_to_file()

    def delete(self, id):
        """
        Sterge task cu id dat
        :param id: id-ul dupa care se sterge
        :type id: int
        :return: task-ul sters
        :rtype:Task
        """

        try:
            task_to_delete = self.__data[id]
            del self.__data[id]
            self.__save_to_file()
            return task_to_delete
        except KeyError:
            raise RepositoryError("No task with given id.")

    def get_all(self) -> list:
        """
        Returneaza intreaga lista de task-uri
        """
        return list(self.__data.values())

    def size(self):
        return len(self.__data)
