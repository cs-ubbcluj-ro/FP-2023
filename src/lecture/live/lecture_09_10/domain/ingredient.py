import unittest

from lecture.live.lecture_09_10.domain.idobject import IdObject


class Ingredient(IdObject):
    def __init__(self, _id: int, name: str):
        super().__init__(_id)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        if len(new_value) < 5:
            raise ValueError("Name must have at least length 5")
        if type(new_value) != str:
            raise TypeError("Name must be string")
        self.__name = new_value

    def __str__(self):
        return str(self.id) + " -> " + self.name
