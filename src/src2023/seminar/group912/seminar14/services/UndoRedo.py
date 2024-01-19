from src2023.seminar.group912.seminar14.domain.student import Student
from src2023.seminar.group912.seminar14.repo.repository import Repository


class UndoRedoAction:
    """
    Base class for each undo-able / redo-able action
    """

    def undo(self):
        raise NotImplementedError()

    def redo(self):
        raise NotImplementedError()


"""
    For each action that is concrete, we implement a corresponding class 
"""


class AddStudentUR(UndoRedoAction):
    def __init__(self, studentRepo: Repository, student: Student):
        self.__repo = studentRepo
        self.__student = student

    def undo(self):
        self.__repo.delete(self.__student.id)

    def redo(self):
        self.__repo.store(self.__student)


class UndoRedoService:
    def __init__(self):
        self.__history = []
        # std::vector<UndoRedoAction>

    def register(self, operation: UndoRedoAction):
        pass

    # NOTE Structure should be similar to undo/redo from seminar 11
