from src2023.seminar.group912.seminar14.domain.idobject import IdObject


class Student(IdObject):
    def __init__(self, Id: int, name: str):
        super().__init__(Id)
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return str(self.id) + " | " + str(self.__name)
