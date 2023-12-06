from datetime import date

from src2023.seminar.group912.seminar10.domain.car import Car
from src2023.seminar.group912.seminar10.domain.client import Client


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
