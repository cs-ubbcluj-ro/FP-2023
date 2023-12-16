class RepositoryException(Exception):
    def __init__(self, error_message):
        self._error_msg = error_message

    @property
    def message(self):
        return self._error_msg

    def __str__(self):
        return "Repo Exception: " + str(self.message)


class DuplicateCNPException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "There already is a person with that CNP.")


class PersonDoesNotExistException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Person with the given CNP does not exist.")

class AssignmentAlreadyExistsException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "There already is an assignment with that ID.")

class AssignmentDoesNotExistException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "There is no assignment with that ID.")