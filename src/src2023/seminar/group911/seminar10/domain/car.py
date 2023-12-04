class Car:
    def __init__(self, lPlate, make, model, color):
        self.__license_plate = lPlate
        self.__make = make
        self.__model = model
        self.__color = color

    @property
    def license_plate(self):
        return self.__license_plate

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
    def color(self, newColor: str):
        self.__color = newColor

    def __str__(self):
        return self.license_plate + " " + self.make + " " + self.model + " " + self.color

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False

        return self.license_plate == other.license_plate
