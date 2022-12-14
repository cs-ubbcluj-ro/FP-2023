from lecture.live.lecture_09_10.domain.idobject import IdObject
from lecture.live.lecture_09_10.domain.recipe import Recipe


class Product(IdObject):
    def __init__(self, _id: int, name: str, quantity: int, recipe: Recipe):
        super().__init__(_id)
        self._name = name
        self._quantity = quantity
        self._recipe = recipe

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    @property
    def recipe(self):
        return self._recipe
