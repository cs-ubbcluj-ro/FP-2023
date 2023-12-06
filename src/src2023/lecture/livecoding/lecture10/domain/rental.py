import random
from datetime import date, timedelta

from src2023.lecture.livecoding.lecture10.domain.car import Car, generate_cars
from src2023.lecture.livecoding.lecture10.domain.client import Client, generate_clients


class Rental:
    def __init__(self, id: int, car: Car, client: Client, start: date, end: date):
        if not isinstance(id, int) or id < 0:
            raise TypeError("Id must be a positive integer.")

        if not isinstance(car, Car):
            raise TypeError("Car is not... a car.")

        if not isinstance(client, Client):
            raise TypeError("The client ain't a client bro.")

        if not isinstance(start, date) or not isinstance(end, date):
            raise TypeError("The dates must be of type date.")

        self.__id = id
        self.__car = car
        self.__client = client
        self.__start = start
        self.__end = end

    def __str__(self):
        return f'ID: {self.id}\nCar: {self.car}\nClient: {self.client}\nStart Date: {self.start}\nEnd Date: {self.end}'

    def __len__(self):
        return (self.end - self.start).total_seconds() // (3600 * 24)

    @property
    def id(self):
        return self.__id

    @property
    def car(self):
        return self.__car

    @property
    def client(self):
        return self.__client

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end


def generate_rentals(n):
    cars = generate_cars(n)
    clients = generate_clients(n)
    _id = 500

    rentals = []
    for i in range(n):
        # Generate random car and client
        car = random.choice(cars)
        client = random.choice(clients)

        # Generate random start and end dates
        start_date = date.today() + timedelta(days=random.randint(-60, -10))
        end_date = start_date + timedelta(days=random.randint(1, 10))

        # Create a rental object
        rentals.append(Rental(_id + i, car, client, start_date, end_date))

    return rentals


for r in generate_rentals(100):
    print(r)
    print("\n")
