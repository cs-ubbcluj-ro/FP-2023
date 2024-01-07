from src2023.lecture.livecoding.lecture12.domain.flight import Flight
from src2023.lecture.livecoding.lecture12.repo.FligthRepo import RepoError


class MemoryRepository:
    def __init__(self):
        # key is id property value of IdObject, value is object itself
        self._data = {}

    def add(self, object: Flight):
        if not isinstance(object, Flight):
            raise TypeError("Can only add Flight instances")

        if object.id in self._data.keys():
            raise RepoError("Flight already exists")

        self._data[object.id] = object

    def remove(self, _id: int) -> Flight:
        if self.find(_id) is None:
            raise RepoError("Object doesn't exist.")

        return self._data.pop(_id)

    def find(self, _id: int) -> Flight:
        """
        Find car with given license plate
        :param _id:
        :return: Car instance, or None if car with license plate was not found
        """

        # condition ? if True : if False
        return self._data[_id] if _id in self._data.keys() else None
