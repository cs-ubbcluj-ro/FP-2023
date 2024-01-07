class FunctionCall:
    # this implements the Command design pattern
    def __init__(self, f_name, *f_params):
        # *f_params is variable number of arguments
        self.__fname = f_name
        self.__fparams = f_params

    def call(self):
        return self.__fname(*self.__fparams)  # () function call operator

    def __call__(self, *args, **kwargs):
        """
        Overloads the function call operator -> ()
        """
        return self.call()


class Operation:
    def __init__(self, undo_function: FunctionCall, redo_function: FunctionCall):
        self.__undo_function = undo_function
        self.__redo_function = redo_function

    def undo(self):
        self.__undo_function()  # we use the () operator
        # self.__undo_function.call() # <=> to the line above

    def redo(self):
        self.__redo_function()


class CascadedOperation:
    """
    this implments the Composite design pattern
    https://refactoring.guru/design-patterns/composite
    """
    def __init__(self, *operations):
        self.__operations = operations

    def undo(self):
        for oper in self.__operations:
            oper.undo()

    def redo(self):
        for oper in self.__operations:
            oper.redo()


class UndoError(Exception):
    pass


class UndoService:

    def __init__(self):
        # history of program operations
        self.__history = []
        # where we are in the __history
        self.__index = -1

    def record_undo(self, operation: Operation):
        self.__history.append(operation)
        self.__index = len(self.__history) - 1

    def undo(self):
        if self.__index == -1:
            raise UndoError("No more undos")
        self.__history[self.__index].undo()
        # we go back 1 operation
        self.__index -= 1

    def redo(self):
        # TODO check this
        if self.__index == len(self.__history) - 1:
            raise UndoError("No more redos")
        # we go forward 1 operation
        self.__index += 1
        self.__history[self.__index].redo()


if __name__ == "__main__":
    def my_function(a, b):
        return a + b


    f = FunctionCall(my_function, 5, 4)
    print(f.call())
    print(f())
