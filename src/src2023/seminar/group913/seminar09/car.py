class Car:
    def __init__(self, age):
        self.__age = age

    """
    getter / setter for car age
    """

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age < 0:
            raise ValueError("Back to the future!")
        self.__age = new_age

    """
    property for car age
    """

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_value):
        self.set_age(new_value)


if __name__ == "__main__":
    """
    This code is nice because Car class controls acccess to
    its internal representation
    """
    my_car = Car(5)
    print(my_car.get_age())
    # Happy B-day, car!
    my_car.set_age(my_car.get_age() + 1)
    print(my_car.get_age())
    # my_car.set_age(my_car.get_age() - 10)

    """
    This code is nicer because Car class controls access to
    its internal representation, and the code is cleaner
    """
    print(my_car.age)
    my_car.age = 1
    print(my_car.age)
    my_car.age += 2
    print(my_car.age)
    # properties look like fields but are actually methods
    my_car.age -= 10
