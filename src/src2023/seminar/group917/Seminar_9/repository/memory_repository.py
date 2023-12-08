

class TaskInMemoryRepository:
    def __init__(self):
        self.__task_list = []

    def store(self, task):
        """
        Adauga un task in lista de task-uri
        :param task: task-ul de adaugat
        :type task: Task
        :return: -; lista de task-uri se modifica prin adaugarea la sfarsit a task-ului dat
        :rtype: -;
        :raises: ValueError daca exista deja task cu id-ul dat
        """


        if self.find(task.get_id()):
            raise ValueError("Exista deja task cu acest id.")
        self.__task_list.append(task)


    def find(self, id):
        """
        Gaseste task-ul cu id dat
        :param id: id-ul cautat
        :type id: int
        :return: task-ul cu id dat
        :rtype: Task
        """
        for task in self.__task_list:
            if task.get_id() == id:
                return task
        return None

    def delete(self, id):
        """
        Sterge task cu id dat
        :param id: id-ul dupa care se sterge
        :type id: int
        :return: task-ul sters
        :rtype:Task
        """

        task_to_delete = self.find(id)
        if task_to_delete is None:
            raise ValueError("Nu exista task cu id dat.")

        self.__task_list.remove(task_to_delete)
        return task_to_delete

    def get_all(self) -> list:
        """
        Returneaza intreaga lista de task-uri
        """
        return self.__task_list

    def size(self):
        return len(self.__task_list)
