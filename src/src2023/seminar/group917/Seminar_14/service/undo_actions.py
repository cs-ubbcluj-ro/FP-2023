class Action:

    def execute(self):
        raise NotImplementedError()


class UndoAddAction(Action):
    def __init__(self, repo, addedStudent):
        print('ID repo', id(repo))
        self._repo = repo
        self._addedStudent = addedStudent

    @property
    def data(self):
        return self._addedStudent

    def execute(self):
        self._repo.delete_student(self._addedStudent)


class RedoAddAction(Action):
    def __init__(self, repo, addedStudent):
        super().__init__()
        self._repo = repo
        self._addedStudent = addedStudent

    @property
    def data(self):
        return self._addedStudent

    def execute(self):
        self._repo.add_student(self._addedStudent)


# Can also have UndoRedoAction, with methods undo, redo instead of separate classes with execute
# method
# Both redo and undo for an action use the same data

class UndoRedoAction:
    def undo(self):
        raise NotImplementedError()

    def redo(self):
        raise NotImplementedError()


class UndoRedoAddAction(UndoRedoAction):
    def __init__(self, repo, addedStudent):
        super().__init__()
        self._repo = repo
        self._addedStudent = addedStudent

    @property
    def data(self):
        return self._addedStudent

    def undo(self):
        self._repo.delete_student(self._addedStudent)

    def redo(self):
        self._repo.add_student(self._addedStudent)

# Why inheritance: even if Python would let us have UndoAddAction,
# UndoRemoveAction etc in the list of undo/redo/undo+redo actions  ->
# not all programming languages do -> in C++ we would have
# std::vector<Action*> undoActions/std::vector<unique_ptr<Action>> undoActions;

