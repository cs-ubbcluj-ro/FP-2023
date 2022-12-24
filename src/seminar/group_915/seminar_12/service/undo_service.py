"""
ways to implement undo/redo

1. deep copy repositories
    similar to Memento design pattern https://refactoring.guru/design-patterns/memento

2. remember the operations that the program made
    Command design pattern https://refactoring.guru/design-patterns/command

3. state-diffing
    remember the changes between consecutive versions of the repo

"""
from typing import Callable


class command:
    def __init__(self, fun_name: Callable, *fun_params):
        self._fun_name = fun_name
        self._fun_params = fun_params

    def call(self):
        return self._fun_name(*self._fun_params)

    def __call__(self, *args, **kwargs):
        return self.call()


class operation:
    def __init__(self, undo_command: command, redo_command: command):
        self._undo_command = undo_command
        self._redo_command = redo_command

    def undo(self):
        # NOTE calls the undo command via () operator overload
        self._undo_command()

    def redo(self):
        self._redo_command()


class UndoRedoError(Exception):
    pass


class UndoService:
    def __init__(self):
        # we keep the history of the program's operations here
        self._history = []
        self._index = -1

    def record(self, op: operation):
        self._history.append(op)
        self._index += 1

    def undo(self):
        if self._index == -1:
            raise UndoRedoError("No more undos")

        self._history[self._index].undo()
        self._index -= 1

    def redo(self):
        if self._index == len(self._history) - 1:
            raise UndoRedoError("No more redos")

        self._history[self._index + 1].redo()
        self._index += 1


if __name__ == "__main__":
    def a(x, y, z, t):
        return x + y + z + t


    def b(x):
        return x ** 3


    function_a = command(a, 1, 2, 3, 4)
    print(function_a.call())
    print(function_a())

    # cmd = lambda function_name, function_params: function_name(*function_params)
    # undo = cmd(a, [1, 2, 3, 4])
    # print(cmd(a, [1, 2, 3, 4]))
    # print(cmd(b, [30]))
