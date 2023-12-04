from datetime import date

from src2023.seminar.group913.seminar10.domain.car import Car
from src2023.seminar.group913.seminar10.domain.client import Client


class Rental:
    """
    One rental object represents one client who rented one car

    Each rental object has:
        -> id : str
        -> client : Client (who rented the car)
        -> car : Car (car that was rented)
        -> start, end : date (renting interval)
    """

    def __init__(self, id: str, client: Client, car, start, end):
        if not isinstance(client, Client):
            raise TypeError("Client must be of type Client")

        if not isinstance(car, Car):
            raise TypeError("Car must be of type Car")

        if not isinstance(start, date):
            raise TypeError("Start must be of type date")
        if not isinstance(end, date):
            raise TypeError("End must be of type date")

        self.__id = id
        self.__client = client
        self.__car = car
        self.__start = start
        self.__end = end

    @property
    def id(self):
        return self.__id

    @property
    def client(self):
        return self.__client

    @property
    def car(self):
        return self.__car

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    def __eq__(self, other):
        if not isinstance(other, Rental):
            return False

        return self.id == other.id
