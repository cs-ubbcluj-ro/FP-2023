from src2023.seminar.group914.seminar14.domain.student import Student
from src2023.seminar.group914.seminar14.repo.repository import Repo


class UndoRedoAction:
    """
    This is the base class for all actions that can be undone/redone
    It raises NotImplementedError because those methods need to be
    overriden
    """

    def undo(self):
        raise NotImplementedError()

    def redo(self):
        raise NotImplementedError()


class AddStudentUR(UndoRedoAction):
    def __init__(self, repo: Repo, student: Student):
        self.__repo = repo
        self.__student = student

    def undo(self):
        self.__repo.delete_student(self.__student.id)

    def redo(self):
        self.__repo.add_student(self.__student)


class StudentService:
    def __init__(self, student_repo: Repo):
        self.__repo = student_repo
        self.__undo = []
        self.__redo = []

    def add_student(self, student: Student):
        # TODO Validation
        self.__repo.add_student(student)
        # If there was no exception, record operation for undo/redo

        # doing something invalidates all redo's
        self.__redo.clear()
        self.__undo.append(AddStudentUR(self.__repo, student))

    def undo(self):
        if len(self.__undo) == 0:
            raise Exception("No more undos")

        # take operation off the undo stack, undo it and then
        # add it to the redo stack
        undo = self.__undo.pop()
        undo.undo()
        self.__redo.append(undo)

    def redo(self):
        pass
