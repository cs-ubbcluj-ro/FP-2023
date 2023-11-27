from src2023.seminar.group911.seminar09.car import Car, getNCars


class RepositoryError(Exception):
    """
    RepositoryError is a type of Exception
    - works in try ... except clauses
    """
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
        pass

    def remove(self, license_plate: str) -> Car:
        """
        Remove the car with the given license plate
        :param license_plate:
        :return: The removed car
        Raise RepositoryError if car not in repo
        """
        pass

    @property
    def all(self):
        """
        Property to return all cars in repo
        :return:
        """
        pass

    def __len__(self):
        """
        Return no. of cars in repository
        :return:
        """
        pass


def test_CarRepositoryMemory():
    repo = CarRepositoryMemory()
    assert len(repo) == 0

    # try to add some cars
    cars = getNCars(5)  # hope license plates are unique!
    repo_len = 0
    for c in cars:
        repo.add(c)
        repo_len += 1
        assert len(repo) == repo_len

    # try to add a duplicate car
    try:
        repo.add(cars[0])
        assert False  # car must not be added
    except RepositoryError:
        assert True  # we expect an exception here

    # try to remove cars
    repo_len = 5
    for c in cars:
        assert repo.remove(c.license_plate) == c
        repo_len -= 1
        assert len(repo) == repo_len

    # try to remove inexisting car
    try:
        repo.remove(cars[0].license_plate)
        assert False  # we expected an error
    except RepositoryError:
        assert True  # error was raised, everything ok

test_CarRepositoryMemory()