from src2023.seminar.group912.seminar14.domain.idobject import IdObject



class Laboratory(IdObject):
    def __init__(self, _id: int, name):
        super().__init__(_id)
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return str(self.id) + " | " + str(self.__name)
