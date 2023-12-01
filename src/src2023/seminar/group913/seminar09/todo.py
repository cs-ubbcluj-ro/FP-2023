"""
1. Write a Car class
    private fields:
         __licence_plate
         __make
         __model
         __color

    properties
        only get for the __licence_plate, __make, __model
        get/set for __color

    methods
        constructor (must set all fields)
        __str__ (return a one-line str with the Car's info)
        __eq__ (==, return true if and only if the cars have same
                licence plates)

2. Write a generate_cars(n : int) -> list method
    - method generates a list of "n" cars
    - license plates should be valid (pick a few counties - [AB, CJ, B, TL])
    - make/model/color combined from a defined list
"""
import random


class Car:
    def __init__(self, license_plate: str, make: str, model: str, color: str):
        self.__license_plate = license_plate
        self.__make = make
        self.__model = model
        self.__color = color

    @property
    def make(self) -> str:
        return self.__make

    @property
    def license_plate(self) -> str:
        return self.__license_plate

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, value) -> None:
        self.__color = value

    def __str__(self) -> str:
        return f"Car [License Plate: {self.__license_plate}, Make: {self.__make}, Model: {self.__model}, Color: {self.__color}]"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Car):
            return NotImplemented

        return self.__license_plate == other.__license_plate


def generate_cars(n: int) -> list:
    cars = []

    random_colors = ["Red", "Blue", "Green", "Yellow",
                     "Black", "White", "Grey", "Orange", "Purple", "Pink"]
    random_makes = ["Toyota", "Honda", "Ford", "Chevrolet",
                    "Nissan", "BMW", "Mercedes", "Audi", "Volkswagen", "Hyundai"]
    random_models = ["Model 1", "Model 2", "Model 3", "Model 4"]

    random_couties = ["AB", "CJ", "B", "BC", "BH", "BT", "BV", "BR", "BZ", "CL", "CS", "CT", "CV", "DB", "DJ", "GL", "GR", "GJ",
                      "HR", "HD", "IL", "IS", "IF", "MM", "MH", "MS", "NT", "OT", "PH", "SM", "SJ", "SB", "SV", "TR", "TM", "TL", "VL", "VS", "VN"]

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(n):
        color = random_colors[random.randint(0, len(random_colors) - 1)]
        model = random_models[random.randint(0, len(random_models) - 1)]
        make = random_makes[random.randint(0, len(random_makes) - 1)]
        countie = random_couties[random.randint(0, len(random_couties) - 1)]

        two_digit_number = random.randint(10, 99)
        random_string = ""
        for _ in range(3):
            random_string += letters[random.randint(0, len(letters) - 1)]

        license_plate = f"{countie} {two_digit_number} {random_string}"

        cars.append(Car(license_plate, make, model, color))

    return cars


if __name__ == "__main__":
    car_list = generate_cars(10)
    for car in car_list:
        print(car)