class FunctionCall:
    def __init__(self, fun_name, *fun_params):
        self.__fun_name = fun_name
        self.__fun_params = fun_params

    def call(self):
        return self.__fun_name(*self.__fun_params)

    def __call__(self, *args, **kwargs):
        # overload the function call operator -- ()
        return self.call()


class Operation:
    def __init__(self, fundo: FunctionCall, fredo: FunctionCall):
        self.__fundo = fundo
        self.__fredo = fredo

    def undo(self):
        return self.__fundo()  # <=> to self.__fundo.call()

    def redo(self):
        return self.__fredo()


class UndoError(Exception):
    pass


class UndoService:
    def __init__(self):
        # history of the program's operations
        self.__history = []
        self.__index = 0

    def record(self, oper: Operation):
        self.__history.append(oper)
        self.__index += 1

    def undo(self):
        if self.__index == 0:
            raise UndoError("No more undos")
        self.__index -= 1
        self.__history[self.__index].undo()

    def redo(self):
        if self.__index >= len(self.__history):
            raise UndoError("No more redos")
        self.__history[self.__index].redo()
        self.__index += 1


if __name__ == "__main__":
    def fun_undo(a, b, c):
        return a + b + c


    def fun_redo(a, b, c):
        return a * b * c


    fundo = FunctionCall(fun_undo, 1, 2, 3)
    fredo = FunctionCall(fun_redo, 10, 20, 30)
    o = Operation(fundo, fredo)
    print(o.undo())
    print(o.redo())
