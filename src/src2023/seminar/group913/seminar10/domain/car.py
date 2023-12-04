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
            return False

        return self.__license_plate == other.__license_plate
