from seminar.group_912.seminar_11.domain.car import car
from random import choice, randint
import pickle


# RepoException inherits from Python's builtin Exception class
# RepoException "IS AN" exception
class RepoException(Exception):
    pass


class car_repo(object):
    def __init__(self):
        # keys are car license numbers, values are car objects
        self._data = {}

    def add(self, new_car: car):
        if new_car.car_id in self._data:
            raise RepoException("Car already in repo")
        self._data[new_car.car_id] = new_car

    def get(self, car_id: str):
        # If car cannot be found in repo, catch the dict's KeyError and
        # re-raise it as RepoException
        try:
            return self._data[car_id]
        except KeyError:
            raise RepoException("Car is not in repo")

    def get_all(self):
        return list(self._data.values())

    def __len__(self):
        return len(self._data)


class car_repo_bin_file(car_repo):
    def __init__(self, file_name="cars.bin"):
        # call superclass constructor
        super().__init__()
        # remember the name of the file we're working with
        self._file_name = file_name
        # load the cars from the file
        self._load_file()

    def add(self, new_car: car):
        # call the add() method on the super class
        # we want to do everything the superclass add() already does
        super().add(new_car)
        # we also want to save all cars to a text file
        self._save_file()

    def _load_file(self):
        # r - read, b - binary
        obj = []
        try:
            fin = open(self._file_name, "rb")
            obj = pickle.load(fin)
            fin.close()
        except FileNotFoundError:
            pass

        for c in obj:
            super().add(c)

    def _save_file(self):
        # w - write mode (overwrite), b - binary mode
        fout = open(self._file_name, "wb")
        pickle.dump(self.get_all(), fout)
        # NOTE Don't forget to close the file!
        fout.close()


# just a plain old regular class :)
class car_repo_text_file(car_repo):
    # this class inherits from car_repo
    # => has all the mathods and attributes in car_repo

    def __init__(self, file_name="cars.txt"):
        # call superclass constructor
        super().__init__()
        # remember the name of the file we're working with
        self._file_name = file_name
        # load the cars from the file
        self._load_file()

    def _load_file(self):
        """
        Load the cars from a text file
        """
        # open a text file for reading
        # t - text file mode, r - reading
        lines = []

        try:
            fin = open(self._file_name, "rt")
            # each car should be on its own line
            lines = fin.readlines()
            # close the file when done reading
            fin.close()
        except IOError:
            # It's ok if we don't find the input file
            pass

        for line in lines:
            current_line = line.split(",")
            new_car = car(current_line[0].strip(), current_line[1].strip(), current_line[2].strip(),
                          current_line[3].strip())
            # NOTE call super() so that we don't write the file we're reading from
            super().add(new_car)

    def _save_file(self):
        """
        Save all cars to a text file
        """
        # open a text file for writing
        # t - text file mode, w - writing (rewrite the file every time)
        fout = open(self._file_name, "wt")

        # writes car_string into the text file
        # fout.write(car_string)
        for car in self.get_all():
            car_string = str(car.car_id) + "," + str(car.make) + "," + str(car.model) + "," + str(car.color) + "\n"
            fout.write(car_string)

        # call close when done writing
        fout.close()

    def add(self, new_car: car):
        # call the add() method on the super class
        # we want to do everything the superclass add() already does
        super().add(new_car)
        # we also want to save all cars to a text file
        self._save_file()


#
# def test_car_repo():
#     repo = car_repo()
#     # car repository is empty
#     assert len(repo) == 0
#
#     # add cars to the repo
#     c1 = car("CJ 01 ABC", "Dacia", "Sandero", "red")
#     repo.add(c1)
#     c2 = car("CJ 01 XYZ", "Dacia", "Logdy", "white")
#     repo.add(c2)
#     assert len(repo) == 2
#
#     # try to add the same car again
#     try:
#         repo.add(c1)
#         assert False
#     except RepoException:
#         assert True
#
#     # retrieve cars from repo
#     assert repo.get("CJ 01 ABC") == c1
#
#     # TODO Try to implement repo["CJ 01 XYZ"] == c2
#     assert repo.get("CJ 01 XYZ") == c2
#
#     # try to retrieve a non-existing car
#     try:
#         repo.get("SJ 04 RTY")
#         assert False
#     except RepoException:
#         assert True


def generate_cars(n: int):
    """
    Generates n car instances
    :return: A list of n cars
    """
    counties = ["AB", "SJ", "VS", "CJ", "B", "TL", "TR", "GL", "GR", "IS"]
    make_model = {"Dacia": ["Logan", "Sandero", "Lodgy"], "Toyota": ["Corolla", "RAV-4", "Yaris"]}
    colors = ["red", "blue", "green", "black"]

    result = []
    while n > 0:
        letters = ""
        for i in [0, 1, 2]:
            letters += chr(randint(65, 90))  # A -> Z
        car_id = choice(counties) + " " + str(randint(10, 99)) + " " + letters
        make = choice(list(make_model.keys()))
        model = choice(make_model[make])
        color = choice(colors)
        result.append(car(car_id, make, model, color))
        n -= 1
    return result


if __name__ == "__main__":
    # repo = car_repo()
    # repo_text = car_repo_text_file()
    # # NOTE Save the generated cars to the file
    # for c in generate_cars(10):
    #     print(str(c))
    #     # repo.add(c)
    #     repo_text.add(c)

    # read the cars.bin input file
    car_repo_bin = car_repo_bin_file()
    car_list = generate_cars(20)
    for c in car_list:
        car_repo_bin.add(c)

    print("Cars saved in cars.bin")
    for c in car_repo_bin.get_all():
        print(str(c))

    # read the cars.txt file
    # car_repo_text = car_repo_text_file()
    # print("\n\nCars saved in cars.txt")
    # for c in car_repo_text.get_all():
    #     print(str(c))

    # NOTE Load the cars and display them again
    # new_car_repo = car_repo_text_file()
    # for c in new_car_repo.get_all():
    #     print(str(c))
