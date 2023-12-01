from src2023.seminar.group911.seminar09.car import Car, getNCars
import pickle


class RepositoryError(Exception):
    """
    RepositoryError is a type of Exception
    - works in try ... except clauses
    """
    # FIXME Add an __init__ with a message
    pass


class CarRepositoryBinary:
    def __init__(self):
        # cars are stored in this dict
        self.__data = {}  # keys are license plates
        # load all cars from the binary file
        try:
            self.__load_file()
        except FileNotFoundError:
            print("Oopsie!")
        except OSError:
            raise RepositoryError()

    def add(self, car: Car):
        """
        Add a new car to the repo
        :param car:
        :return:
        Raise RepositoryError if car with license plate
        already in repo
        """
        # FIXME a bug here
        if car.license_plate in self.__data:
            raise RepositoryError
        self.__data[car.license_plate] = car
        self.__save_file()

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
            self.__save_file()
            return car
        else:
            raise RepositoryError

    def __save_file(self):
        # TODO Call each time the dict of cars is updated
        file = open("cars.data", "wb")  # w - write, b - binary
        pickle.dump(self.__data, file)
        file.close()

    def __load_file(self):
        file = open("cars.data", "rb")  # r - read, b - binary
        self.__data = pickle.load(file)
        file.close()

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


if __name__ == "__main__":

    repo = CarRepositoryBinary()
    for car in getNCars(5):
        repo.add(car)

    for c in repo.all:
        print(c)

    # cars = getNCars(10)
    # for c in cars:
    #     print(c)

    # 1. Write to a binary file using Pickle
    # file = open("cars.data","wb") # w - write, b - binary
    # pickle.dump(cars,file)
    # file.close()

    # 2. Read from binary file
    # file = open("cars.data", "rb")  # r - read, b - binary
    # my_cars = pickle.load(file)
    # file.close()
    #
    # for c in my_cars:
    #     print(c)
