from rational import Rational


class Calculator:
    def __init__(self):
        self.__value = Rational()
        self.__history = [Rational()]

    def add(self, q: Rational):
        self.__value += q
        self.__history.append(self.__value)

    def value(self):
        return self.__value

    def undo(self):
        if len(self.__history) == 1:
            raise ValueError("No more undos")
        last_value = self.__history.pop()
        self.__value = self.__history[-1]
