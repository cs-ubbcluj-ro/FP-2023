from domain.person import Person
from domain.task import Task


class Assignment:

    def __init__(self, id: int, task, person, eval: float):
        self._id = id
        self._task = task
        self._person = person
        self._eval = eval
    #Read about @property: https://realpython.com/python-property/
    @property
    def id(self):
        return self._id

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, task):
        self._task = task

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, person):
        self._person = person

    @property
    def evaluation(self):
        return self._eval

    @evaluation.setter
    def evaluation(self, evaluation):
        self._eval = evaluation


    def __eq__(self, other):
        return self._id == other.id
    def __str__(self):
        return "Assignment ID: "+ str(self.id) +'| Task: ['+ str(self._task) + '] | Person: [' + str(self._person)+']a'


if __name__ == "__main__":
    task = Task(1, 'gdhskjfhg', 12, 9, "pending")
    person = Person('1920909292123', 'Marcel')
    assignment = Assignment(1, task, person, 7)
    print(assignment.task)
    print(assignment.id)