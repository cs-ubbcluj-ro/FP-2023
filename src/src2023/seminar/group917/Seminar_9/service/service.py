from src2023.seminar.group917.Seminar_9.domain.task import Task


class TaskController:
    def __init__(self, repository):
        self.__repo = repository

    def add_task(self, id, descriere: str, zi: int, luna: int, status: str) -> None:
        """
        Adauga un task in lista de task-uri
        :param task_list: lista de task-uri
        :type task_list: list
        :param task: task-ul de adaugat
        :type task: dict
        :return: -; modifica lista prin adaugarea la sfarsit a task-ului
        :rtype:
        :raises: ValueError daca task-ul de adaugat nu este valid, daca task-ul exista deja
        """

        task = Task(id, descriere, zi, luna, status)
        self.__repo.store(task)

    def delete_task(self, id: int):
        """
        Sterge task dupa id
        :param id: id dupa care se sterge
        :type id: int
        :return: task-ul sters
        :rtype: Task
        :raises: ValueError daca nu exista task cu id dat
        """
        return self.__repo.delete(id)


    def filter_by_description(self, description: str) -> list:
        """
        Returneaza lista cu task-urile care contin in descriere un string dat
        :param task_list: lista de task-uri
        :param description: substring-ul dupa care se cauta
        :return: o lista in care se regasesc doar task-urile care au in descriere string-ul dat
        """
        return [task for task in self.__repo.get_all() if description.lower() in task.get_descriere().lower()]

    def get_report_by_day(self) -> dict:
        """
        Face un raport de activitati pe data
        :param task_list: lista de task-uri
        :return: dictionar cu cheie data (str format din zi si luna) si valoare lista
                aferenta de task-uri care au deadline in ziua respectiva
        """
        day_dictionary = {}
        for task in self.__repo.get_all():
            if task.get_date() in day_dictionary:
                day_dictionary[task.get_date()].append(task)
            else:
                day_dictionary[task.get_date()] = [task]
        return day_dictionary

    def get_all_tasks(self) -> list:
        """
        Returneaza lista cu toate task-urile

        """
        return self.__repo.get_all()

    def add_default_tasks(self):
        self.add_task(1, 'Read book', 11, 10, 'pending')
        self.add_task(2, 'Host movie marathon', 5, 8, 'done')
        self.add_task(3, 'Travel to uncharted island', 10, 1, 'in-progress')
        self.add_task(4, 'Build treehouse', 12, 9, 'pending')
        self.add_task(5, 'Book Skydiving Adventure', 4, 4, 'done')
        self.add_task(6, 'Learn to ski', 21, 11, 'done')
        self.add_task(7, 'Master Art of Origami', 5, 8, 'in-progress')
        self.add_task(8, 'Dance to 80\'s music', 12, 9, 'pending')
        self.add_task(9, 'Learn to play guitar', 12, 9, 'done')
        self.add_task(10, 'Listen to Christmas music', 30, 12, 'done')