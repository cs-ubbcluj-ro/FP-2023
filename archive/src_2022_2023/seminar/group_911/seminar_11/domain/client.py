class Client:
    def __init__(self, client_id, cnp, name):
        self._client_id = client_id
        self._cnp = cnp
        self._name = name

    @property
    def id(self):
        return self._client_id

    @property
    def cnp(self):
        return self._cnp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __eq__(self, z):
        """
        Two Clients are equal if they have the same id
        :param z:
        :return:
        """
        if type(z) != Client:
            return False
        return self.id == z.id

    def __str__(self):
        return "Id=" + str(self.id) + ", Name=" + str(self.name)

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    c1 = Client(100, "280122334506070", "Pop Maria")
    c2 = Client(101, "2334506070", "Pop Maria")
    print(id(c1), id(c2))
    # Note fun with == __eq__
    print(c1 == [])
