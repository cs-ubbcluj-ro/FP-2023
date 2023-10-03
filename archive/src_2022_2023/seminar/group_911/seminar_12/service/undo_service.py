"""
Ways to implement undo/redo

1. remember the program's state before each operation
(deep copy list/dict/repository)
Memento design pattern -- https://refactoring.guru/design-patterns/memento

2. carry out the opposite of each operation (undo) or redo the operation
itself (redo)
Command design pattern -- https://refactoring.guru/design-patterns/command

3. state-diffing
What are the differences in the program before/after the operation?
"""


class call():
    def __init__(self, func_name, *func_params):
        self._func_name = func_name
        self._func_params = func_params

    def call(self):
        return self._func_name(*self._func_params)


class operation():
    def __init__(self, undo: call, redo: call):
        self._undo = undo
        self._redo = redo

    def undo(self):
        self._undo.call()

    def redo(self):
        self._redo.call()


class cascaded_operation():
    def __init__(self, *operations):
        self._operations = operations

    def undo(self):
        for oper in self._operations:
            oper.undo()

    def redo(self):
        for oper in self._operations:
            oper.redo()


class UndoRedoError(Exception):
    pass


class UndoService:
    def __init__(self):
        self._operations = []
        self._index = 0
        # flag == true means operation is not from undo_service
        # flag == false means don't record for undo/redo
        self._undo_flag = True

    def record_for_undo(self, op: operation):
        # this is a callback from undo_service so it should not be recorded
        if self._undo_flag is False:
            return
        # NOTE this isn't actually complete
        self._operations.append(op)
        # update the undo/redo index to the latest value
        self._index = len(self._operations)

    def undo(self):
        if self._index == 0:
            raise UndoRedoError("No more undos")

        self._undo_flag = False
        self._operations[self._index - 1].undo()
        self._undo_flag = True
        self._index -= 1

    def redo(self):
        if self._index >= len(self._operations):
            raise UndoRedoError("No more redos")
        self._undo_flag = False
        self._operations[self._index].redo()
        self._undo_flag = True
        self._index += 1


if __name__ == "__main__":
    def a(x, y, z, t):
        return x + y + z + t


    def b(x):
        return x ** 2


    call_b = call(b, 11)
    call_a = call(a, 1, 2, 3, 4)
    # ... other things ...
    print(call_a.call())
    print(call_b.call())
