class Car:
    def __init__(self, license_plate: str, make: str, model: str, color: str):
        # self.__license_plate is a private field
        self.__license_plate = license_plate
        # self.make is a property setter
        self.make = make
        self.model = model
        self.color = color

    @property
    def license(self):
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

    @make.setter
    def make(self, new_make: str):
        self.__make = new_make

    @model.setter
    def model(self, new_model: str):
        self.__model = new_model

    @color.setter
    def color(self, new_color: str):
        self.__color = new_color

    # repr is the str representation of the object
    # called by data structures when str()-ing them
    def __repr__(self):
        return str(self)

    def __str__(self):
        display_str = f"{self.__license_plate}, {self.make} {self.model}," \
                      f" {self.color}"

        return display_str

if __name__ == "__main__":
    car = Car("CJ 01 ABC", "Audi", "A1", "blue")
    print(car)
    print(car.license)
    car.make = "Toyota"
    print(car)
