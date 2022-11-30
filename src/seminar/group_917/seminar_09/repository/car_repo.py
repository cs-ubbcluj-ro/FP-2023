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

    def __len__(self):
        return len(self.__data)


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
        f = open(self._car_files, "rt")  # r - read, t - text mode
        for car_line in f.readlines():
            tokens = car_line.split(",")
            # NOTE - Parse away whitespace (including the \n, including in tokens)
            # NOTE - Mind the types
            # NOTE - We assume input files are correct
            c = car(tokens[0], tokens[1], tokens[2], tokens[3])

            # car_repo_text_file.add(self,c)
            self.add(c)

            # super().add(c)

    def _save_file(self):
        # NOTE - What happens if we can't open the file in writing?
        # raise RepoError(...)
        pass


repo = car_repo_text_file("../cars.txt")

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
