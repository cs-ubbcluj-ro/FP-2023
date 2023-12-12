class Command:
    def __init__(self, fun_name, *fun_params):
        self.__fun_name = fun_name
        self.__fun_params = fun_params

    def call(self):
        return self.__fun_name(*self.__fun_params)

    def __call__(self, *args, **kwargs):
        return self.call()


class Operation:
    def __init__(self, undo_command: Command, redo_command: Command):
        self.__undo = undo_command
        self.__redo = redo_command

    def undo(self):
        return self.__undo()

    def redo(self):
        return self.__redo()


def my_function(a, b, c, d, e):
    return a + b * c + d + e


cmd = Command(my_function, 1, 2, 3, 4, 5)
cmd()


class UndoRedoError(Exception):
    pass


class UndoService:
    def __init__(self):
        self.__undo = []
        self.__redo = []

    def register(self, oper: Operation):
        self.__undo.append(oper)

    def undo(self):
        if not self.__undo:
            raise UndoRedoError("No more undos!")

        o = self.__undo.pop()
        self.__redo.append(o)
        o.undo()

    def redo(self):
        if not self.__redo:
            raise UndoRedoError("No more redos!")

        o = self.__redo.pop()
        self.__undo.append(o)
        o.redo()

# def myFun(*args, **kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))

# Driver code
# myFun('Geeks', 'for', 'Geeks', mid="abcd")
