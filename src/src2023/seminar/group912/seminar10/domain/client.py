# Ciupe Marius Daniel
class Client:
    def __init__(self, id: int, name: str):
        if not isinstance(id, int):
            raise TypeError("Id cannot be non-integer.")

        if not isinstance(name, str):
            raise TypeError("Name must be of type str.")

        self.__id = id
        self.__name = name

    def __str__(self):
        return f'ID: {self.id}; Name: {self.name}'

    def __eq__(self, other):
        return self.id == other.id

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
