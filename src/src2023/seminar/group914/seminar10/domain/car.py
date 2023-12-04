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
