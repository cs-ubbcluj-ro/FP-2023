from car import generate_cars, Car
import pickle

from src2023.seminar.group912.seminar09.car_repository_memory import RepositoryError


class CarRepositoryBinary:
    def __init__(self, file_name: str = "data.bin"):
        # key is car license plate, value is car object
        self.__data = {}
        self.__file_name = file_name
        self.__load_file()

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
        self.__save_file()

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
        self.__save_file()

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

    def __load_file(self):
        try:
            file = open(self.__file_name, "rb")  # r - read, b - binary
            self.__data = pickle.load(file)
            file.close()
        # Exceptions that are not FileNotFoundError are still raised and crash the program?
        except FileNotFoundError:
            # TODO Should be replaced with logging
            print("Generate new repo")

    def __save_file(self):
        file = open(self.__file_name, "wb")  # w - write, b - binary
        pickle.dump(self.__data, file)  # write the whole dict
        file.close()

    def __len__(self):
        """
        Return the number of cars in repository
        :return:
        """
        return len(self.__data)


if __name__ == "__main__":
    # cars = generate_cars(10)

    # for c in cars:
    #     print(c)

    # file = open("cars.data", "wb")  # w - write, b - binary
    # pickle.dump(cars, file)
    # file.close()

    # file = open("cars.data", "rb")  # r - read, b - binary
    # my_cars = pickle.load(file)
    # file.close()
    #
    # for c in my_cars:
    #     print(c)

    bin_repo = CarRepositoryBinary()
    for c in bin_repo.all:
        print(c)

    for c in generate_cars(5):
        bin_repo.add(c)

    # bin_repo.__load_file()
