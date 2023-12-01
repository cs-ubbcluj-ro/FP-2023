"""
1. Write a Car class
    private fields:
         __license_plate // CJ 01 ABC
         __make // Toyota
         __model // Corolla
         __color // red

    properties
        only get for the __licence_plate, __make, __model
        get/set for __color

    methods
        constructor (must set all fields)
        __str__ (return a one-line str with the Car's info)
        __eq__ (==, return true if and only if the cars have same
                license plates)

2. Write a generate_cars(n : int) -> list method
    - method generates a list of "n" cars
    - license plates should be valid (pick a few counties - [AB, CJ, B, TL])
    - make/model/color combined from a defined list
"""
import random
import string


class Car:
    def __init__(self, licence_plate, make, model, color):
        self.__licence_plate = licence_plate
        self.__make = make
        self.__model = model
        self.__color = color

    @property
    def licence_plate(self):
        return self.__licence_plate

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    # in line string
    def __str__(self):
        return "Car with ID: " + self.__licence_plate + " | make: " + self.__make + " " + self.__model + " | color: " + self.__color

    # equal licence plates check
    def __eq__(self, car2):
        if not isinstance(car2, Car):
            return False
        return self.__licence_plate == car2.licence_plate

    @staticmethod
    def generate():
        # generate plate
        counties = ["AB", "VS", "NT", "CJ", "BC", "IS"]
        letters = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(
            string.ascii_uppercase)
        plate = random.choice(counties) + str(random.randint(10, 99)) + letters

        # generate make
        makes = ["Opel", "Dacia", "Nissan"]
        make = random.choice(makes)

        # generate model
        models = ["1st Gen", "2nd Gen", "3rd Gen", "Electric"]
        model = random.choice(models)

        # generate color
        colors = ["Grey", "Black", "Red", "Yellow"]
        color = random.choice(colors)

        return Car(plate, make, model, color)


def generate_n_cars(n: int) -> []:
    arr = []
    for i in range(n):
        arr.append(Car.generate())
    return arr


def start():
    n = int(input(">"))
    arr = generate_n_cars(n)

    for car in arr:
        print(str(car))

# start()
# print(Car("x","A","B","red") == "abc")
