class car:
    """
    Add a new car to the car pool. Each car must have
        -> a valid license plate number,
        -> a make and model taken from a list of makes and models.
        -> each car will have a color.
    """

    def __init__(self, car_id: str, make: str, model: str, color: str):
        self.__car_id = car_id
        self.__make = make
        self.__model = model
        self.__color = color

    @property
    def car_id(self):
        return self.__car_id

    @car_id.setter
    def car_id(self, new_value):
        self.__car_id = new_value


def test_car():
    new_car = car("CJ 01 ABC", "Dacia", "Sandero", "red")
    # assert new_car.get_id() == "CJ 01 ABC"
    assert new_car.car_id == "CJ 01 ABC"
    assert new_car.make == "Dacia"
    assert new_car.model == "Sandero"
    assert new_car.color == "red"
    assert str(new_car) == "CJ 01 ABC -> Dacia Sandero, red"

    # repaint it
    # new_car.set_color("blue")
    new_car.color = "blue"
    assert new_car.color == "blue"
    assert str(new_car) == "CJ 01 ABC -> Dacia Sandero, blue"

    # change license plates
    new_car.car_id = "CJ 99 XYZ"
    assert str(new_car) == "CJ 99 XYZ -> Dacia Sandero, blue"


if __name__ == "__main__":
    test_car()
