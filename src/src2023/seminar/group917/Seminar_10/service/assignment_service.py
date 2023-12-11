from collections import defaultdict

from src2023.seminar.group917.Seminar_10.domain.assignment import Assignment


class AssignmentService:

    def __init__(self, task_repo, person_repo, assignment_repo, assignment_validator):
        self.__task_repo = task_repo
        self.__person_repo = person_repo
        self.__assignment_repo = assignment_repo
        self.__assignment_validator = assignment_validator

    # We assume we only read id_task and cnp of person from console
    def create_assignment(self, id_assignment, id_task, cnp, evaluation):
        """
        Add assignment
        :raises: RepositoryException if there is no task with given id
                 PersonDoesNotExistException daca nu exista persoana cu CNP dat
                 AssignmentValidationException daca nota evaluarii nu este valida

        """

        task = self.__task_repo.get(id_task)

        person = self.__person_repo.get(cnp)

        assignment = Assignment(id_assignment, task, person, evaluation)
        self.__assignment_validator.validate(assignment)
        self.__assignment_repo.add(assignment)

    def get_all(self):
        return self.__assignment_repo.all

    #TO-DO: add reports, undo