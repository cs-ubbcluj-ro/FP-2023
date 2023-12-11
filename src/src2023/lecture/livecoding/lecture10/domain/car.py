import random

from src2023.lecture.livecoding.lecture10.domain.idobject import IdObject


class Car(IdObject):
    # class Car inherits from class IdObject
    def __init__(self, _id, licence, make, model, color):
        super().__init__(_id)
        self.__license_plate = licence
        self.__make = make
        self.__model = model
        self.__color = color

    def __str__(self):
        return f'{self.id} - {self.license}, {self.make} {self.model}, {self.color}'

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.license == other.license

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

    @color.setter
    def color(self, new_color):
        self.__color = new_color


def generate_cars(n: int) -> list:
    LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    counties = ['AB', 'CJ', 'B', 'TL', 'IS', 'CT', 'DB', 'GR']
    make = ['Toyota', 'Audi', 'Dacia', 'Mazda', 'Peugeot']
    model = ['Auris', 'Corola', 'Logan', 'series 3', 'series 4', 'series 5']
    color = ['blue', 'red', 'yellow', 'black', 'white', 'silver']
    _id = 100
    car_list = []

    for i in range(n):
        numbers = str(random.randint(0, 9)) + str(random.randint(0, 9))
        letters = random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS)
        car_list.append(Car(_id + i, f'{random.choice(counties)} {numbers} {letters}',
                            random.choice(make),
                            random.choice(model),
                            random.choice(color)))

    return car_list


# for c in generate_cars(5):
#     print(c)

# c = Car(100,"abcd","a","t","r")
# c.color=4
# print(c.color)