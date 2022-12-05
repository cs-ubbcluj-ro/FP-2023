from random import randint, choice
import pickle
from seminar.group_917.seminar_09.domain.car import car


# RepoError inherits from Exception class => RepoError IS AN exception
class RepoError(Exception):
    pass


class car_repo:
    def __init__(self):
        self.__data = {}

    def add(self, new_car: car):
        # if one of the dict's keys is new_car.car_id
        if new_car.car_id in self.__data:
            raise RepoError("Car already added to repo")
        self.__data[new_car.car_id] = new_car

    def get(self, car_id):
        try:
            return self.__data[car_id]
        except KeyError:
            raise RepoError("Car not in repo")

    def get_all(self):
        # NOTE dict values_view is not a sequence by default
        return list(self.__data.values())

    def __len__(self):
        return len(self.__data)


# TODO How can we redo this inheritance to minimize code duplication?
class car_repo_bin_file(car_repo):
    def __init__(self, file: str = "cars.bin"):
        super().__init__()
        self._car_files = file
        self._load_file()

    def add(self, new_car: car):
        # Add the car to repo, validation, etc.
        super().add(new_car)
        # Save the updated repo of cars to file
        self._save_file()

    def _load_file(self):
        # r - read mode, b - binary file
        fin = open(self._car_files, "rb")
        car_list = pickle.load(fin)
        fin.close()
        for c in car_list:
            # call super() so we don't deal with files
            super().add(c)

    def _save_file(self):
        # w - write mode, b - binary file
        fout = open(self._car_files, "wb")
        # serialize, marshal with pickle -> write to a binary file, or
        # to a network socket, or some remote procedure call (RPC)
        pickle.dump(self.get_all(), fout)
        fout.close()


class car_repo_text_file(car_repo):
    """
    I want this class to do everything car_repo already does, and:
        -> load cars from a text file on initialization
        -> save cars to a text file on any change
    """

    def __init__(self, file: str = "cars.txt"):
        super().__init__()
        self._car_files = file
        self._load_file()

    def add(self, new_car: car):
        # Add the car to repo, validation, etc.
        super().add(new_car)
        # Save the updated repo of cars to file
        self._save_file()

    def _load_file(self):
        # NOTE Calling code might not know about FileNotFoundError but it should
        # NOTE know about RepoError
        try:
            f = open(self._car_files, "rt")  # r - read, t - text mode
        except FileNotFoundError:
            raise RepoError("Input file not found")

        for car_line in f.readlines():
            tokens = car_line.split(",")
            # .strip() away the end-line terminator
            c = car(tokens[0], tokens[1], tokens[2], tokens[3].strip())

            # car_repo_text_file.add(self,c)
            self.add(c)

            # super().add(c)

    def _save_file(self):
        # w - write mode (overwrite each time), t - text file
        fout = open(self._car_files, "wt")
        for c in self.get_all():
            car_str = c.car_id + "," + c.make + "," + c.model + "," + c.color + "\n"
            fout.write(car_str)
        fout.close()


def generate_cars(n: int):
    models_list = {"Dacia": ["Logan", "Sandero", "Spring"], "VW": ["Polo", "Golf", "Passat", "Arteon"],
                   "Toyota": ["Corolla", "Yaris", "Prius"], "Audi": ["A3", "A4", "A4 Sedan", "Q5"]}
    colors_list = ["black", "white", "blue", "red", "metallic", "beige", "green"]
    county_list = ["CJ", "B", "MM", "SV", "CT", "BT", "IS", "BH", "IF"]

    makes_list = list(models_list.keys())
    cars_list = []
    for i in range(n):
        given_make = choice(makes_list)
        given_model = choice(models_list[given_make])
        given_color = choice(colors_list)
        given_county = choice(county_list)
        letter_1 = randint(0, 25)
        letter_2 = randint(0, 25)
        letter_3 = randint(0, 25)

        # so we can get numbers such as 01, 02, 09, ...
        number = str(randint(0, 9)) + str(randint(0, 9))

        licence_plate = given_county + " " + number + " " + chr(65 + letter_1) + chr(
            65 + letter_2) + chr(
            65 + letter_3)
        our_car = car(licence_plate, given_make, given_model, given_color)
        cars_list.append(our_car)
    return cars_list


# Generate some cars and write them to a text-file backed repository
# cars = generate_cars(10)
print("Cars in text file")
repo = car_repo_text_file()
for c in repo.get_all():
    print(c)

print("\n\nCars in binary file")
bin_repo = car_repo_bin_file()
for car in bin_repo.get_all():
    print(car)

# Load the cars into another repository :)
# print("\n\nCars in new repo")
# new_repo = car_repo_text_file()
# for c in new_repo.get_all():
#     print(c)

#
# def test_car_repo():
#     repo = car_repo()
#     # repo should be empty at start
#     assert len(repo) == 0
#
#     c1 = car("CJ 01 ABC", "VW", "Polo", "black")
#     c2 = car("SJ 01 TTR", "Dacia", "Logan", "white")
#     # add some cars
#     repo.add(c1)
#     repo.add(c2)
#     assert len(repo) == 2
#
#     # cannot add the same car twice
#     try:
#         repo.add(c1)
#         assert False
#     except RepoError:
#         assert True
#     # retreive cars from repo
#     assert repo.get("SJ 01 TTR") == c2
#     # NOTE Try to implement so that this works: repo["CJ 01 ABC"] == c1
#     assert repo.get("CJ 01 ABC") == c1
#
#     # cannot retrieve cars not in repo
#     try:
#         repo.get("IS 98 ABC")
#         assert False
#     except RepoError:
#         assert True
