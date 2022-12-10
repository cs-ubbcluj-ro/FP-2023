from random import randint

from seminar.group_912.seminar_10.car import Car


# This class inherits from Exception
class RepoException(Exception):
    pass


class CarRepoIterator():
    def __init__(self, car_repo):
        self._repo = car_repo
        # start iteration at the beginning of the list
        self._index = -1

    def __next__(self):
        if self._index == len(self._repo) - 1:
            raise StopIteration()

        self._index += 1
        return self._repo._cars[self._index]


class CarRepo:
    def __init__(self):
        self._cars = []

    def add_car(self, new_car: Car):
        for car in self._cars:
            if new_car.license == car.license:
                raise RepoException("Duplicate license plates")
        self._cars.append(new_car)

    def get_all_cars(self):
        return self._cars

    def get_car_by_license_plate(self, license_plate: str):
        for car in self._cars:
            if car.get_license_plate() == license_plate:
                return car
        raise RepoException("Car not found!")

    def remove_car(self, license_plate: str):
        car = self.get_car_by_license_plate(license_plate)
        self._cars.remove(car)

    def update_car(self, license_plate: str, model: str, color: str, make: str):
        car = self.get_car_by_license_plate(license_plate)
        car.set_model(model)
        car.set_color(color)
        car.set_make(make)

    def __iter__(self):
        return CarRepoIterator(self)

    def __len__(self) -> int:
        return len(self._cars)

    def __str__(self) -> str:
        string = ""
        for car in self._cars:
            string += str(car) + "\n"
        return string


def gen_cars(n):
    car_list = []

    counties = ["CJ", "HD", "MM", 'SV', "TM"]
    make_model = [["VW", "Golf", "Polo", "Passat"], ["BMW", "E36", "M5 CS", "1 Series"],
                  ["Renault", "Laguna", "Megane", "Clio"], ["Mercedes", "C63 AMG", "GLE 550", "E220"]]
    colors = ["Red", "Green", "Grey", "Black", "Magenta", "Blue", "Light Pink"]

    for i in range(n):
        car_nr = randint(0, 3)
        # 65 is the ASCII code for A
        plate = f"{counties[randint(0, 4)]} {randint(0, 9)}{randint(1, 9)} {chr(randint(65, 90))}{chr(randint(65, 90))}{chr(randint(65, 90))}"
        make = make_model[car_nr][0]
        model = make_model[car_nr][randint(1, 3)]
        color = colors[randint(0, 6)]
        car = Car(plate, make, model, color)
        car_list.append(car)

    return car_list


if __name__ == "__main__":
    cars = gen_cars(10)
    repo = CarRepo()
    for car in cars:
        repo.add_car(car)

    # print(len(repo))
    # print(repo)
    for car in repo:
        print(car)
