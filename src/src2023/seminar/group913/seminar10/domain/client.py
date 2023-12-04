class Client:
    """
    fields set in class constructor (id, name)
    getter properties for
        -> id : str
        -> name : str

    -> __eq__ overwritten
        - two clients are == if they have the same id
    """

    def __init__(self, id: str, name: str):
        if not isinstance(id, str):
            raise TypeError()
        if not isinstance(name, str):
            raise TypeError()

        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return self.id == other.id

        # TODO NOT to do like below
        # try:
        #     return self.id == other.id
        # except AttributeError: # don't use this error :)
        #     return False

    def __str__(self):
        return f"Client id: {self.id}, name: {self.name}"


cf = Client("1234", "Dorel")
print(cf == 100)
