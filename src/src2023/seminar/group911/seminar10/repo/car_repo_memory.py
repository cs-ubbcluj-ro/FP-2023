import random

from src2023.seminar.group911.seminar10.domain.car import Car


class RepositoryError(Exception):
    """
    RepositoryError is a type of Exception
    - works in try ... except clauses
    """
    # FIXME Add an __init__ with a message
    pass


class CarRepositoryMemory:
    def __init__(self):
        # cars are stored in this dict
        self.__data = {}  # keys are license plates

    def add(self, car: Car):
        """
        Add a new car to the repo
        :param car:
        :return:
        Raise RepositoryError if car with license plate
        already in repo
        """
        if car.license_plate in self.__data:
            raise RepositoryError
        self.__data[car.license_plate] = car

    def remove(self, license_plate: str) -> Car:
        """
        Remove the car with the given license plate
        :param license_plate:
        :return: The removed car
        Raise RepositoryError if car not in repo
        """
        if license_plate in self.__data:
            car = self.__data[license_plate]
            del self.__data[license_plate]
            return car
        else:
            raise RepositoryError

    @property
    def all(self) -> list:
        """
        Property to return all cars in repo
        :return:
        """
        return list(self.__data.values())

    def __len__(self):
        """
        Return no. of cars in repository
        :return:
        """
        return len(self.__data.values())

    def __iter__(self):
        # FIXME Implement a proper iterator here
        return list(self.__data.values()).__iter__()


def getRndLetter():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters[random.randint(0, len(letters) - 1)]


def generateLicensePlate():
    return "CJ " + str(random.randint(10, 99)) + " " + getRndLetter() + getRndLetter() + getRndLetter()


def getNCars(n):
    myList = []
    for i in range(n):
        myList.append(Car(generateLicensePlate(), "Toyota", "Carolla", "red"))

    return myList


repo = CarRepositoryMemory()
for car in getNCars(5):
    repo.add(car)

for c in repo:
    print(c)
