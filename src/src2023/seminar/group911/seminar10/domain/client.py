class Client:
    def __init__(self, id: str, name: str):
        if not isinstance(id, str) or not isinstance(name, str):
            raise ValueError("Bad argument types")
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return "{id}, {name}".format(id=self.id, name=self.name)

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return other.id == self.id
