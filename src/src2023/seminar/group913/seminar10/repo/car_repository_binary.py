import pickle

from src2023.seminar.group913.seminar09.car_repository_memory import RepositoryError
from src2023.seminar.group913.seminar09.todo import Car, generate_cars


class CarRepositoryBinaryFile:
    def __init__(self, file_name: str):
        # we keep the program's cars here
        # __data is private, so the class controls access to it
        self.__file_name = file_name
        self.__data = {}
        # we load the input file
        self.__load_file()

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
        self.__save_file()

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

        result = self.__data.pop(licence_plate)
        self.__save_file()
        return result

    def get_all(self) -> list:
        """
        Return all cars in repo
        :return:
        """
        return list(self.__data.values())

    def __save_file(self):
        """
        This method is private because:
            1. The class is responsible for writing its state to file
            2. We want file operations to be unseen to the user
        """
        file = open(self.__file_name, "wb")  # w - write, b - binary
        pickle.dump(self.__data, file)  # write the car_list to a binary file
        file.close()

    def __load_file(self):
        try:
            file = open(self.__file_name, "rb")  # r - read, b - binary
            self.__data = pickle.load(file)
            file.close()
        except FileNotFoundError:
            print("We ate this exception. It was yummy!")
        except OSError:
            # the UI does not know we use files :)
            raise RepositoryError("Cannot start repository")

    def __len__(self):
        """
        Return the number of cars in the repository
        :return:
        """
        return len(self.__data)


bin_repo = CarRepositoryBinaryFile("mycars.data")

for car in bin_repo.get_all():
    print(car)

# for car in generate_cars(10):
#     bin_repo.add(car)
