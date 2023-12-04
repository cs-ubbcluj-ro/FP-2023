import string
import random

from src2023.seminar.group914.seminar10.domain.car import Car


class RepositoryError(Exception):
    """
    RepositoryError inherits from Exception
    """
    pass


class CarRepoIterator():
    def __init__(self, all_cars):
        self.__cars = all_cars
        self.__pos = -1

    def __next__(self):
        self.__pos += 1

        if self.__pos == len(self.__cars):
            # no more cars
            # signal the calling loop to stop
            raise StopIteration()

        return self.__cars[self.__pos]


class CarRepoMemory:
    """
    In-memory repository for the Car domain entity
    """

    def __init__(self):
        # this is where we'll store the cars
        self.__data = {}

    def add(self, new_car: Car):
        """
        Add a new car to the repo
        :param new_car:
        :return:
        Raise RepositoryError if car with this license plate already in repo
        """
        if new_car.licence_plate in self.__data:
            raise RepositoryError()
        self.__data[new_car.licence_plate] = new_car

    def get(self, licence_plate: str) -> Car:
        """
        Return car with given license plate
        :param licence_plate:
        :return: The car or None, if given car not in repo
        """

        # V1 - slower because of 2 time dict access
        # if licence_plate not in self.__data:
        #     return None
        # return self.__data[licence_plate]

        # V2 - slower because an exception might have to be built
        try:
            return self.__data[licence_plate]
        except KeyError:
            return None

    def remove(self, licence_plate: str) -> Car:
        """
        Delete car from repo
        :param licence_plate:
        :return: The car that was removed, or None if given car not in repo
        """
        if licence_plate not in self.__data:
            return None
        del self.__data[licence_plate]  # TODO To be tested

    def get_all(self) -> list:
        """
        Return all cars in repo
        :return:
        """
        return list(self.__data.values())

    def __str__(self):
        pass

    def __len__(self):
        """
        Return the number of cars in the repo
        :return:
        """
        return len(self.__data)

    def __iter__(self):
        return CarRepoIterator(list(self.__data.values()))


def generate():
    # generate plate
    counties = ["AB", "VS", "NT", "CJ", "BC", "IS"]
    letters = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(
        string.ascii_uppercase)
    plate = random.choice(counties) + str(random.randint(10, 99)) + letters

    # generate make
    makes = ["Opel", "Dacia", "Nissan"]
    make = random.choice(makes)

    # generate model
    models = ["1st Gen", "2nd Gen", "3rd Gen", "Electric"]
    model = random.choice(models)

    # generate color
    colors = ["Grey", "Black", "Red", "Yellow"]
    color = random.choice(colors)

    return Car(plate, make, model, color)


def generate_n_cars(n: int) -> []:
    arr = []
    for i in range(n):
        arr.append(generate())
    return arr


if __name__ == "__main__":
    repo = CarRepoMemory()
    for c in generate_n_cars(10):
        # print(c)
        repo.add(c)

    for car in repo:
        print(car)
