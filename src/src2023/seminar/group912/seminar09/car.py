import random


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


def generate_cars(n: int) -> list:
    LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    counties = ['AB', 'CJ', 'B', 'TL']
    make = ['Toyota', 'Audi', 'NuStiu']
    model = ['Auris', 'Corola']
    color = ['blue', 'red', 'yellow']
    car_list = []

    for i in range(n):
        numbers = str(random.randint(0, 9)) + str(random.randint(0, 9))
        letters = random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS)
        car_list.append(Car(f'{random.choice(counties)} {numbers} {letters}',
                            random.choice(make),
                            random.choice(model),
                            random.choice(color)))

    return car_list


if __name__ == "__main__":
    cars = generate_cars(10)
    for c in cars:
        print(c)
