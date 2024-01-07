from src2023.lecture.livecoding.lecture10.domain.idobject import IdObject


class RepositoryError(Exception):
    pass


class RepoIterator:
    def __init__(self, data: list):
        self.__data = data
        self.__pos = -1

    def __next__(self):
        # return the next item we iterate over
        self.__pos += 1
        if self.__pos == len(self.__data):
            raise StopIteration()
        return self.__data[self.__pos]


class MemoryRepository:
    def __init__(self):
        # key is id property value of IdObject, value is object itself
        self._data = {}

    def add(self, object: IdObject):
        """
        Add a new car to repository
        :param object:
        :return:
        Raise RepositoryError if car with license plate already in repo, in which case car
        is not added
        """
        if not isinstance(object, IdObject):
            raise TypeError("Can only add IdObject instances")

        if object.id in self._data.keys():
            raise RepositoryError("Car already exists")

        self._data[object.id] = object

    def remove(self, _id: int) -> IdObject:
        """
        Remove IdObject with given id plate from repository
        :param _id:
        :return: The car that was removed
        Raise RepositoryError if car with license plate is not in the repository
        """
        if self.find(_id) == None:
            raise RepositoryError("Object doesn't exist.")

        return self._data.pop(_id)

    def find(self, _id: int) -> IdObject:
        """
        Find car with given license plate
        :param _id:
        :return: Car instance, or None if car with license plate was not found
        """

        # condition ? if True : if False
        return self._data[_id] if _id in self._data.keys() else None

    def __iter__(self):
        """
        This is the Iterator design pattern
        https://refactoring.guru/design-patterns/iterator
        """
        return RepoIterator(list(self._data.values()))

    def __getitem__(self, item):
        if item not in self._data:
            return None
        return self._data[item]

    def __len__(self):
        """
        Return the number of cars in repository
        :return:
        """
        return len(self._data)

# r = MemoryRepository()
# r.remove(100)
