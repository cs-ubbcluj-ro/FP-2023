"""
ways to implement undo/redo

1. copy the repository(ies) at each undo-able step
    -> deep copy wastes (a lot of) memory
    -> Memento design pattern https://refactoring.guru/design-patterns/memento

2. remember the operation itself and do its opposite (undo) or do it again (redo)
    -> does not waster memory
    -> Command design pattern https://refactoring.guru/design-patterns/command

3. state-diffing
    -> the difference between versions of the repository


"""


class UndoRedoError(Exception):
    pass


class call():
    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def run(self):
        # () -- call operator
        return self._function_name(*self._function_params)

    def __call__(self, *args, **kwargs):
        return self.run()


class operation:
    def __init__(self, undo_call: call, redo_call: call):
        self._undo_call = undo_call
        self._redo_call = redo_call

    def undo(self):
        # self._undo_call.run()
        self._undo_call()

    def redo(self):
        self._redo_call()


class cascaded_operation():
    def __init__(self, *operations):
        self._operations = operations

    def undo(self):
        for op in self._operations:
            op.undo()

    def redo(self):
        for op in self._operations:
            op.redo()


class UndoService:
    def __init__(self):
        self._history = []
        self._index = 0
        self._undo_redo_flag = True

    def record(self, op: operation):
        if self._undo_redo_flag is False:
            return
        self._history = self._history[:self._index]
        self._history.append(op)
        self._index = len(self._history)

    def undo(self):
        if self._index == 0:
            raise UndoRedoError("No more undos")

        # NOTE Don't record anything for undo/redo, as wel are already
        # undoing things
        self._undo_redo_flag = False
        self._history[self._index - 1].undo()
        self._undo_redo_flag = True
        self._index -= 1

    def redo(self):
        if self._index == len(self._history):
            raise UndoRedoError("No more redos")

        self._undo_redo_flag = False
        self._history[self._index].redo()
        self._undo_redo_flag = True
        self._index += 1


if __name__ == "__main__":
    def a(x, y, z, t):
        return x + y + z + t


    print(a(1, 2, 3, 4))
    call_a = call(a, 10, 20, 30, 40)
    # print(call_a.run())
    print(call_a())
