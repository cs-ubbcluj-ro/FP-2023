from src2023.lecture.livecoding.lecture10.domain.car import Car


class RepositoryError(Exception):
    pass


class CarRepoIterator:
    def __init__(self, data: list):
        self.__data = data
        self.__pos = -1

    def __next__(self):
        # return the next item we iterate over
        self.__pos += 1
        if self.__pos == len(self.__data):
            raise StopIteration()
        return self.__data[self.__pos]


class CarMemoryRepository:
    def __init__(self):
        # key is car license plate, value is car object
        self.__data = {}

    def add(self, car: Car):
        """
        Add a new car to repository
        :param car:
        :return:
        Raise RepositoryError if car with license plate already in repo, in which case car
        is not added
        """
        if car.license in self.__data.keys():
            raise RepositoryError("Car already exists")

        self.__data[car.license] = car

    def remove(self, license_plate: str) -> Car:
        """
        Remove car with given license plate from repository
        :param license_plate:
        :return: The car that was removed
        Raise RepositoryError if car with license plate is not in the repository
        """
        if license_plate not in self.__data.keys():
            raise RepositoryError("Car doesn't exist.")

        return self.__data.pop(license_plate)

    def find(self, license_plate: str) -> Car:
        """
        Find car with given license plate
        :param license_plate:
        :return: Car instance, or None if car with license plate was not found
        """
        return self.__data[license_plate] if license_plate in self.__data.keys() else None

    def __iter__(self):
        """
        This is the Iterator design pattern
        https://refactoring.guru/design-patterns/iterator
        """
        return CarRepoIterator(list(self.__data.values()))

    def __getitem__(self, item):
        if item not in self.__data:
            return None
        return self.__data[item]

    def __len__(self):
        """
        Return the number of cars in repository
        :return:
        """
        return len(self.__data)
