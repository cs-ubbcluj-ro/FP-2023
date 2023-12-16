from domain.domain_exceptions import TaskValidationException, PersonValidationException, AssignmentValidationException


class TaskValidator:
    def __init__(self):
        pass

    def validate(self, task):
        """
        Validates a given task
        :param task: the task that is being validated
        :return: -
        :raises: TaskValidationException daca task-ul nu e valid
        """
        _errors = []
        if len(task.description) < 2:
            _errors.append("Description should have at least two characters.")

        if task.deadline_day > 31 or task.deadline_day < 1:
            _errors.append("Days should be between 1-31.")

        if task.deadline_month > 12 or task.deadline_month < 1:
            _errors.append("Month should be between 1-12.")

        if task.status not in ['pending', 'in-progress', 'done']:
            _errors.append('Incorrect status. Can only be "pending", "in-progress" or "done".')

        if len(_errors) > 0:
            raise TaskValidationException(_errors)


class PersonValidator:
    def __init__(self):
        pass

    def validate(self, person):

        _errors = []
        if len(person.cnp) != 13:
            _errors.append("Incorrect CNP. Should have exactly 13 digits.")

        if len(person.name) < 2:
            _errors.append('Name should have at least 2 characters.')

        if len(_errors) > 0:
            raise PersonValidationException(_errors)


class AssignmentValidator:
    def __init__(self):
        pass

    def validate(self, assignment):
        _errors = []
        if assignment.evaluation > 10 or assignment.evaluation < 1:
            _errors.append("Evaluation incorrect. Should be between 1 and 10.")

        if len(_errors) > 0:
            raise AssignmentValidationException(_errors)
