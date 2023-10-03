from archive.src_2022_2023.lecture.live.lecture_09_10.domain.idobject import IdObject
from archive.src_2022_2023.lecture.live.lecture_09_10.domain.ingredient import Ingredient


class Stock(IdObject):
    def __init__(self, _id: int, ingredient: Ingredient, quantity: int):
        super().__init__(_id)
        self._ingredient = ingredient
        self._quantity = quantity

    @property
    def ingredient(self):
        return self._ingredient

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_value):
        self._quantity = new_value
