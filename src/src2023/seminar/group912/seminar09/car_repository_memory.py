"""
Test - Driven Development
    1. Have the specification of the tested class/function
    2. Write a test for the class/function
    3. Run the test and see it fails
    4. Implement the class so that the test does not fail
    5. Optimize the class
"""
from src2023.seminar.group912.seminar09.car import Car


class RepositoryError(Exception):
    # RepositoryError is a kind of exception
    pass


class CarRepositoryMemory:
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
        if car.licence_plate in self.__data.keys():
            raise RepositoryError("Car already exists")

        self.__data[car.licence_plate] = car

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

    @property
    def all(self):
        """
        Return all cars in repository
        :return:
        """
        return self.__data.values()

    def __len__(self):
        """
        Return the number of cars in repository
        :return:
        """
        return len(self.__data)


def test_CarRepositoryMemory():
    repo = CarRepositoryMemory()
    assert len(repo) == 0

    car0 = Car("CJ 10 ABC", "Dacia", "Lodgy", "black")
    repo.add(car0)
    assert len(repo) == 1
    assert repo.find("CJ 10 ABC") == car0
    assert repo.find("CJ 10 ABD") is None

    # try to add same car again
    try:
        repo.add(car0)
        assert False
    except RepositoryError:
        assert True
    assert len(repo) == 1

    car1 = Car("TL 99 ERT", "Toyota", "RAV4", "red")
    repo.add(car1)
    assert len(repo) == 2

    assert car0 in repo.all
    assert car1 in repo.all
    assert len(repo.all) == 2

    try:
        repo.remove("VS 02 TRE")
        assert False
    except RepositoryError:
        assert True
    assert len(repo.all) == 2

    assert repo.remove("TL 99 ERT") == car1
    assert len(repo) == 1
    assert repo.find("CJ 10 ABC") == car0
    assert repo.find("TL 99 ERT") is None

    assert repo.remove("CJ 10 ABC") == car0
    assert len(repo) == 0
    assert repo.find("CJ 10 ABC") is None
    assert repo.find("TL 99 ERT") is None


test_CarRepositoryMemory()
