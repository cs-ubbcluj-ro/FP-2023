class fun_call():
    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        return self._function_name(*self._function_params)


class operation():
    def __init__(self, undo: fun_call, redo: fun_call):
        self._undo = undo
        self._redo = redo

    def undo(self):
        self._undo.call()

    def redo(self):
        self._redo.call()


class cascade_operation():
    def __init__(self, *operations):
        self._operations = operations

    def undo(self):
        for operation in self._operations:
            operation.undo()

    def redo(self):
        for operation in self._operations:
            operation.redo()


class UndoRedoError(Exception):
    pass


class UndoService:
    """
    Ways to implement undo/redo !?!!

    1. Deep copy the list/dict/repository
        => very inefficient memory wise
        -> Memento design pattern -- https://refactoring.guru/design-patterns/memento

    2. Remember the changes in the program
        -> https://refactoring.guru/design-patterns/command
    command = tell the program what to do, but don't do it now

    3. State-diffing !?

    """

    def __init__(self):
        self._operations = []
        self._index = -1
        # set the flag to False during undo/redo
        self._undo_flag = True

    def record_for_undo(self, op: operation):
        if self._undo_flag is False:
            # ignore recording operations coming from undo/redo
            return
        self._operations.append(op)
        self._index += 1

    def undo(self):
        if self._index == -1:
            raise UndoRedoError("No more undos")
        # NOTE Don't record undo()/redo() operations
        self._undo_flag = False
        self._operations[self._index].undo()
        self._undo_flag = True
        self._index -= 1

    def redo(self):
        if self._index == len(self._operations) - 1:
            raise UndoRedoError("No more redos")
        self._index += 1
        # NOTE Don't record undo()/redo() operations
        self._undo_flag = False
        self._operations[self._index].redo()
        self._undo_flag = True


if __name__ == "__main__":
    def a(x, y, z, t):
        return x + y + z + t


    def b(x):
        return x ** 3


    fc_a = fun_call(a, 10, 20, 30, 40)
    fc_b = fun_call(b, 99)

    print(fc_b.call())
    print(fc_a.call())
