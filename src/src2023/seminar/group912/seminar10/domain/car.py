class Car:
    def __init__(self, licence, make, model, color):
        self.__licence_plate = licence
        self.__make = make
        self.__model = model
        self.__color = color

    def __str__(self):
        return f'{self.licence_plate}, {self.make}, {self.model}, {self.color}'

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.licence_plate == other.licence_plate

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
