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

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @group.setter
    def group(self, new_group):
        self.__group = new_group

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.id == other.id

    def __str__(self):
        return "ID: {} | Name: {} | Group: {}".format(self.id, self.name, self.group)


def test_student():
    s = Student(1, "Popescu Ion", "831")
    assert (s.id == 1)
    assert (s.name == "Popescu Ion")
    assert (s.group == "831")
    print(s)
