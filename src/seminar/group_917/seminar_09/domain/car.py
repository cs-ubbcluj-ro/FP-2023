class car:
    """
    Add a new car to the car pool.
    Each car must have
        -> a valid license plate number,
        -> a make and model taken from a     list of makes and models.
        -> a color.
    """

    def __init__(self, car_id: str, make, model: str, color: str):
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

    def __str__(self):
        return self.car_id + " -> " + self.make + " " + self.model + ", " + self.color


def test_car():
    c = car("CJ 01 ABC", "VW", "Polo", "black")
    assert c.car_id == "CJ 01 ABC"

    # assert c.get_make() == "VW"
    assert c.make == "VW"

    assert c.model == "Polo"
    assert c.color == "black"

    # str representation for a car instance
    assert str(c) == "CJ 01 ABC -> VW Polo, black"
    # update car license plates
    # c.set_id("CJ 99 TYU")
    c.car_id = "CJ 99 TYU"
    assert c.car_id == "CJ 99 TYU"
    # repaint car
    c.color = "red"
    assert c.color == "red"
    # NOTE Changing car make/model does not make sense, so we don't have
    # set methods for those => read-only properties
