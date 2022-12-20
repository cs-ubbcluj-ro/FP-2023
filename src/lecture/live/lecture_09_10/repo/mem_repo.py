from lecture.live.lecture_09_10.domain.idobject import IdObject
from lecture.live.lecture_09_10.domain.ingredient import Ingredient


class RepositoryError(Exception):
    pass


class Repository:

    def __init__(self):
        self._data = {}

    def add(self, id_object: IdObject):
        if not isinstance(id_object, IdObject):
            raise TypeError("Can only add IdObjects to repo!")
        if id_object.id in self._data:
            raise RepositoryError("Object already added")
        self._data[id_object.id] = id_object

    def get(self, object_id):
        return self._data[object_id]

    def __len__(self):
        return len(self._data)


if __name__ == "__main__":
    ingr = Ingredient(100, "abcd")
    # NOTE type() returns the actual type of the object
    print(type(ingr) == IdObject)
    # NOTE isinstance() checks that ingr is also an IdObject => works with inheritance
    print(isinstance(ingr, IdObject))
