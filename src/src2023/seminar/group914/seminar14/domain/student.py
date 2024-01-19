class Student:
    def __init__(self, id: int, name: str, group: str):
        self.__id = id
        self.__name = name
        self.__group = group

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group

    def __str__(self):
        return str(self.id) + " / " + str(self.name) + " / " + str(self.group)
