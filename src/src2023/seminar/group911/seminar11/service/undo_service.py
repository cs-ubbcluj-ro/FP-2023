class FunctionCall:
    def __init__(self, name, *params):
        self.__name = name
        self.__params = params

    def call(self):
        return self.__name(*self.__params)

    def __call__(self, *args, **kwargs):
        return self.call()


class Operation:
    def __init__(self, fc_undo: FunctionCall, fc_redo: FunctionCall):
        self.__undo = fc_undo
        self.__redo = fc_redo

    def undo(self):
        # () - function call operator
        self.__undo()

    def redo(self):
        self.__redo()
        # self.__redo.call()


class UndoError(Exception):
    pass


class UndoService:
    def __init__(self):
        self.__history = []
        self.__index = 0

    def record(self, oper: Operation):
        self.__history.insert(0, oper)

    def undo(self):
        # print("undo", self.__index)
        if self.__index == len(self.__history):
            raise UndoError("No more undos")

        self.__history[self.__index].undo()
        self.__index += 1

    def redo(self):
        # print("redo",self.__index)
        if self.__index == 0:
            raise UndoError("No more redos")

        self.__index -= 1
        self.__history[self.__index].redo()



if __name__ == "__main__":
    def fun_fun_fun(a, b, c, d, e):
        return a + b + c * d + e


    fc = FunctionCall(fun_fun_fun, 2, 3, 4, 5, 6)
    print(fc.call())
    print(fc())
