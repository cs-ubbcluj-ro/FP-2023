from src2023.seminar.group913.seminar09.todo import Car, generate_cars
import pickle


class RepositoryError(Exception):
    """
    RepositoryError is a kind of Exception
    """

    @property
    def message(self) -> str:
        return self.__message

    def __init__(self, message: str = "Not specified Reository Error"):
        self.__message = message

    def __str__(self) -> str:
        return self.__message


class CarRepositoryMemory:
    def __init__(self):
        # we keep the program's cars here
        # __data is private, so the class controls access to it
        self.__data = {}

    def add(self, new_car: Car):
        """
        Add the new car to the repo
        :param new_car:
        :return:
        Raise RepositoryError if car with this license plate already in repo
        """
        if new_car.license_plate in self.__data:
            raise RepositoryError(
                f"Car with license plate {new_car.license_plate} already in repository")

        self.__data[new_car.license_plate] = new_car

    def remove(self, licence_plate: str) -> Car:
        """
        Remove car from repo
        :param license_plate:
        :return:
        Raise RepositoryError if car with license_plate not in repo
        """
        if licence_plate not in self.__data.keys():
            raise RepositoryError(
                f"Car with license plate {licence_plate} not in repository")

        return self.__data.pop(licence_plate)

    def get_all(self) -> list:
        """
        Return all cars in repo
        :return:
        """

        return list(self.__data.values())

    def __len__(self):
        """
        Return the number of cars in the repository
        :return:
        """
        return len(self.__data)


def test_car_repo_memory():
    repo = CarRepositoryMemory()
    assert len(repo) == 0  # repo should be empty

    # try to add cars
    car_list = generate_cars(10)
    repo_len = 0
    for car in car_list:
        repo.add(car)
        repo_len += 1
        assert len(repo) == repo_len

    # try to add the same car twice
    try:
        repo.add(car_list[0])  # this is already in repo
        assert False  # code should raise exception
    except RepositoryError:
        # we expect a RepoError here
        assert True

    repo_len = 10
    # test remove from repository
    for car in car_list:
        # remove returns the car that it deletes
        assert repo.remove(car.license_plate) == car
        repo_len -= 1
        assert len(repo) == repo_len

    assert len(repo) == 0

    # try to remove non existing car
    try:
        repo.remove(car_list[0].license_plate)
        assert False
    except RepositoryError:
        assert True


# test_car_repo_memory()

# 1. Write to binary file
# car_list = generate_cars(10)
# for c in car_list:
#     print(c)
# file = open("cars.data", "wb")  # w - write, b - binary
# pickle.dump(car_list, file)  # write the car_list to a binary file
# file.close()

# 2. Read from binary file
# file = open("cars.data", "rb")  # r - read, b - binary
# cars = pickle.load(file)
# file.close()
#
# for c in cars:
#     print(c)

"""
How do we integrate read/write binary files to the Repository?
"""
