from todo import generate_n_cars, Car
import pickle


class RepositoryError(Exception):
    """
    RepositoryError inherits from Exception
    """
    pass


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
        pass

    def get(self, licence_plate: str) -> Car:
        """
        Return car with given license plate
        :param licence_plate:
        :return: The car or None, if given car not in repo
        """
        pass

    def remove(self, licence_plate: str) -> Car:
        """
        Delete car from repo
        :param licence_plate:
        :return: The car that was removed, or None if given car not in repo
        """
        pass

    def get_all(self) -> list:
        """
        Return all cars in repo
        :return:
        """
        pass

    def __str__(self):
        pass

    def __len__(self):
        """
        Return the number of cars in the repo
        :return:
        """
        pass


"""
    CarRepoBinaryFile should do everything CarRepoMemory already does AND:
        -> save the car list to a binary file after the list of cars is changed
        -> load the car list when starting the repo (??)
"""


class CarRepoBinaryFile(CarRepoMemory):
    """
    CarRepoBinaryFile inherits from CarRepoMemory
        1. all methods in CarRepoMemory are also in CarRepoBinaryFile
        2. we need to add the loadFile() and saveFile() methods
    """

    def __load_file(self):
        # TODO Call from class constructor
        pass

    def __save_file(self):
        # TODO Call from all methods that change the car repo
        pass

    def add(self, new_car: Car):
        # 1. call add from superclass (CarRepoMemory)
        super().add(new_car)
        # 2. if super().add(new_car) raised an Exception we don't run this code
        # 3. if no exception, save the cars into the file
        self.__save_file()


class CarRepoTextFile(CarRepoMemory):
    pass


def test_car_repo():
    # test the repo with these cars
    list_of_cars = generate_n_cars(10)
    car0 = list_of_cars[0]

    car_repo = CarRepoMemory()
    assert len(car_repo) == 0

    for c in list_of_cars:
        car_repo.add(c)
    assert len(car_repo) == 10

    # check that same car cannot be added twice
    try:
        car_repo.add(car0)
        assert False
    except RepositoryError:
        assert True

    for car in list_of_cars:
        # make sure all cars are in the repo
        assert car_repo.get(car.licence_plate) == car

    # check car deletion
    repo_len = 10
    assert len(car_repo) == 10
    for car in list_of_cars:
        assert car_repo.remove(car.licence_plate) == car
        repo_len -= 1
        assert len(car_repo) == repo_len


if __name__ == "__main__":
    # test_car_repo()

    # 1. Write to file -- anytime the repo is changed (add, delete)
    # list_of_cars = generate_n_cars(10)
    # file = open("cars.data", "wb")  # w - write, b - binary
    # pickle.dump(list_of_cars, file)
    # file.close()

    # 2. Read from file (__init__)
    file = open("cars.data", "rb")  # r - read, b - binary
    my_cars = pickle.load(file)
    file.close()

    for c in my_cars:
        print(c)
