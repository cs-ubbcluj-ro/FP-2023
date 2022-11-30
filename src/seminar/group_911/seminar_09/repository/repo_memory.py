from seminar.group_911.seminar_09.domain.car import car
from random import choice, randint


# RepoException inherits from Python's builtin Exception class
# RepoException "IS AN" exception
class RepoException(Exception):
    pass


class car_repo:
    def __init__(self):
        # keys are car license numbers, values are car objects
        self.__data = {}

    def add(self, new_car: car):
        if new_car.car_id in self.__data:
            raise RepoException("Car already in repo")
        self.__data[new_car.car_id] = new_car

    def get(self, car_id: str):
        # If car cannot be found in repo, catch the dict's KeyError and
        # re-raise it as RepoException
        try:
            return self.__data[car_id]
        except KeyError:
            raise RepoException("Car is not in repo")

    def __len__(self):
        return len(self.__data)


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


cars = generate_cars(10)
for c in cars:
    print(str(c))
