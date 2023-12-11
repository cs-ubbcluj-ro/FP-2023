from src2023.seminar.group917.Seminar_10.repository.repo_exceptions import AssignmentDoesNotExistException, AssignmentAlreadyExistsException





class AssignmentInMemoryRepository:
    def __init__(self):
        self.__assignments = {}

    def get(self, assignment_id: int):
        """
        Search for assignment by id
        """
        try:
            assignment = self.__assignments[assignment_id]
            return assignment
        except KeyError:
            raise AssignmentDoesNotExistException()

    def add(self, assignment):
        """
        Add assignment
        :raises: DuplicateIDException if there is already assignment with that id
        """
        if assignment.id in self.__assignments.keys():
            raise AssignmentAlreadyExistsException()
        self.__assignments[assignment.id] = assignment

    def remove(self, assignment_id):
        """
        Remove assignment
        :raises: NonexistentIDException if no assignment with the given ID exists
        """
        try:
            del self.__assignments[assignment_id]
        except KeyError:
            raise AssignmentDoesNotExistException()

    @property
    def all(self):

        return list(self.__assignments.values())

    @property
    def size(self):
        return len(self.__assignments)
