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


def test_car():
    c = car("CJ 01 ABC", "VW", "Polo", "black")
    assert c.get_id() == "CJ 01 ABC"
    assert c.get_make() == "VW"
    assert c.get_model() == "Polo"
    assert c.get_color() == "black"

    # str representation for a car instance
    assert str(c) == "CJ 01 ABC -> VW Polo, black"
    # update car license plates
    c.set_id("CJ 99 TYU")
    assert c.get_id() == "CJ 99 TYU"
    # repaint car
    c.set_color("red")
    assert c.get_color() == "red"
    # NOTE Changing car make/model does not make sense, so we don't have
    # set methods for those => read-only properties
