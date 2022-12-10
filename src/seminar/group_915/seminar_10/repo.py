import random
from random import randint, choice

from seminar.group_915.seminar_10 import Car


def generate_cars(n: int):
    listOfCars = []
    county = ["CJ", "B", "SJ", "BH", "CT"]
    brand_and_model = {"BMW": ["Series 1", "Series 3", "Series 5"], "Audi": ["A1", "A2", "A3"]}
    allColors = ["white", "black", "red", "yellow", "green"]

    for i in range(n):
        nrOfLicensePlate = str(randint(1, 99))
        lettersOfLicensePlate = ""
        for j in range(3):
            lettersOfLicensePlate += chr(randint(65, 90))
        licencePlate = choice(county) + " " + nrOfLicensePlate + " " + lettersOfLicensePlate

        brand = choice(list(brand_and_model.keys()))
        model = choice(brand_and_model[brand])
        color = choice(allColors)

        listOfCars.append(Car(licencePlate, brand, model, color))

    return listOfCars


class RepoException(Exception):
    pass


class CarRepoIterator():
    def __init__(self, car_repo):
        self._repo = car_repo
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # out of cars, so stop iterating
        if self._index >= len(self._repo):
            raise StopIteration()

        self._index += 1
        return self._repo._data[self._index - 1]


class CarRepo:
    def __init__(self):
        self._data = []

    def add_car(self, new_car):
        for cars in self._data:
            if new_car.license_plate == cars.license_plate:
                raise RepoException("Duplicate license plate")
        self._data.append(new_car)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        # we need to return an iterator
        return CarRepoIterator(self)

    def return_all_cars(self):
        return self._data

    def delete_car(self, license_plate):
        for i in range(len(self._data)):
            if self._data[i].license_plate == license_plate:
                self._data.pop(i)
                break


# this class inherits all the fields and methods of CarRepo
# that includes the __iter__ stuff
class CarRepoTextFile(CarRepo):
    def __init__(self):
        # 1. call base class constructor
        super().__init__()
        # 2. load cars from file
        self._load_file()

    def _load_file(self):
        pass

    def _save_file(self):
        # 1. open file for writing in text mode
        fout = open("cars.txt", "wt")
        # 2. loop over all cars
        for car in self:  # should work as this is iterable
            fout.write(car.license_plate + "," + car.make + "," + car.model + "," + car.color + "\n")
        # 3. don't forget to close the file
        fout.close()

    def add_car(self, new_car):
        # call add_car from CarRepo class
        super().add_car(new_car)
        # save the list of cars to file
        self._save_file()


if __name__ == "__main__":
    cars = generate_cars(10)
    car_repo = CarRepoTextFile()
    for car in cars:
        car_repo.add_car(car)
    print(len(car_repo))
    # for car in car_repo.return_all_cars():
    #     print(car)

    # Try to iterate over car_repo
    for car in car_repo:
        # NOTE This might be a problem
        # if random.randint(1,2) == 1:
        #     car_repo.add_car(Car("CJ 99 ERT", "Mazda", "CX-30", "blue"))
        print(car)
