class car:
    """
    Add a new car to the car pool. Each car must have
        -> a valid license plate number,
        -> a make and model taken from a list of makes and models.
        -> each car will have a color.
    """

    def __init__(self, car_id: str, make: str, model: str, color: str):
        pass


def test_car():
    new_car = car("CJ 01 ABC", "Dacia", "Sandero", "red")
    assert new_car.get_id() == "CJ 01 ABC"
    assert new_car.get_make() == "Dacia"
    assert new_car.get_model() == "Sandero"
    assert new_car.get_color() == "red"
    assert str(new_car) == "CJ 01 ABC -> Dacia Sandero, red"

    # repaint it
    new_car.set_color("blue")
    assert new_car.get_color() == "blue"
    assert str(new_car) == "CJ 01 ABC -> Dacia Sandero, blue"

    # change license plates
    new_car.set_id("CJ 99 XYZ")
    assert str(new_car) == "CJ 99 XYZ -> Dacia Sandero, blue"
