from src2023.seminar.group917.Seminar_14.domain.domain import Student
from src2023.seminar.group917.Seminar_14.service.undo_actions import UndoAddAction, RedoAddAction
from src2023.seminar.group917.Seminar_14.utils.ID_generator import IdGeneratorSingleton


class UndoRedoException(Exception):
    pass


class NoMoreRedosException(UndoRedoException):
    pass


class NoMoreUndosException(UndoRedoException):
    pass


class StudentService:
    def __init__(self, repo):
        self.__repo = repo
        self.__id_generator = IdGeneratorSingleton('utils/last_used_id.txt')

        # Much nicer if we put these two lists into an UndoService, and manage
        # everything from there - similar to UndoService from previous seminar

        self.__undo_actions = []
        self.__redo_actions = []

    def add_student(self, name, group):
        id = self.__id_generator.generate_id()
        s = Student(id, name, group)
        # TO-DO: validate student
        # TO-DO: invalidate redos
        self.__undo_actions.append(UndoAddAction(self.__repo, s))
        self.__repo.add_student(s)

    def undo(self):
        # TO-DO: handle case with no more undos

        undo_action = self.__undo_actions.pop()
        undo_action.execute()
        self.__redo_actions.append(RedoAddAction(self.__repo, undo_action.data))

    def redo(self):
        # TO-DO: handle case with no more redos
        action = self.__redo_actions.pop()
        action.execute()
        self.__undo_actions.append(UndoAddAction(self.__repo, action.data))

    def get_all(self):
        return self.__repo.get_all()
