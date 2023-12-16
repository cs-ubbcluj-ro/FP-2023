from collections import defaultdict

from domain.assignment import Assignment
from service.undo_service import Command, Operation


class AssignmentService:

    def __init__(self, undo_service, task_repo, person_repo, assignment_repo, assignment_validator):
        self.__task_repo = task_repo
        self.__person_repo = person_repo
        self.__assignment_repo = assignment_repo
        self.__assignment_validator = assignment_validator
        self.__undo_service = undo_service

    # We assume we only read id_task and cnp of person from console
    def create_assignment(self, id_assignment, id_task, cnp, evaluation):
        """
        Add assignment
        :raises: RepositoryException if there is no task with given id
                 PersonDoesNotExistException daca nu exista persoana cu CNP dat
                 AssignmentValidationException daca nota evaluarii nu este valida

        """

        task = self.__task_repo.get(id_task)

        print(cnp)
        person = self.__person_repo.get(cnp)

        assignment = Assignment(id_assignment, task, person, evaluation)

        self.__assignment_validator.validate(assignment)
        undo_action = Command(self.remove_assignment, id_assignment)
        redo_action = Command(self.create_assignment, id_assignment, id_task, cnp, evaluation)
        operation = Operation(undo_action, redo_action)
        self.__undo_service.record_for_undo(operation)
        self.__assignment_repo.add(assignment)

    def get_all(self):
        return self.__assignment_repo.all

    def filter_assignments(self, person, task):
        result = []
        for assignment in self.__assignment_repo.all:
            if person is not None and assignment.person != person:
                continue
            if task is not None and assignment.task != task:
                continue
            result.append(assignment)
        return result

    def remove_assignment(self, assingment_id):
        deleted_assignment = self.__assignment_repo.get(assingment_id)
        undo_action = Command(self.create_assignment, deleted_assignment.id, deleted_assignment.task.id,
                              deleted_assignment.person.cnp, deleted_assignment.evaluation)
        redo_action = Command(self.remove_assignment, deleted_assignment.id)
        operation = Operation(undo_action, redo_action)
        self.__assignment_repo.remove(assingment_id)

        return operation

    # TO-DO: add reports, undo
