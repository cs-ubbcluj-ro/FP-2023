class Car:
    def __init__(self, color, age):
        self.__color = color
        self.__age = age

    """
    Getters and setters are below
    """

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age < 0:
            raise ValueError("Car too new!")
        self.__age = new_age

    def get_color(self):
        """
        Getter for attribute color
        :return:
        """
        return self.__color

    def set_color(self, new_color):
        """
        Setter for attribute color
        :return:
        """
        self.__color = new_color

    """
    Properties
        - combine the good things about setters/getters and fields
        -> look like fields
        -> methods are called
    """

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.set_age(new_age)


my_car = Car("red", 2)
my_car.set_color("blue")

# this line is not very nice :(
my_car.set_age(my_car.get_age() + 1)  # happy B-day, car!
print(my_car.get_color())

# using properties
print(my_car.age)  # car.age(...) is called
my_car.age = 5  # age can be a read-only property
print(my_car.age)

my_car.age += 1
print(my_car.age)
my_car.age -= 10
