from datetime import date

from src2023.seminar.group911.seminar10.domain.car import Car
from src2023.seminar.group911.seminar10.domain.client import Client


class Rental:
    def __init__(self, id, car, client, start, end):
        if (not isinstance(id, str) or not isinstance(car, Car) or not isinstance(client, Client)
                or not isinstance(start, date) or not isinstance(end, date)):
            raise ValueError("Bad argument types")
        self.__id = id
        self.__car = car
        self.__client = client
        self.__start = start
        self.__end = end

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


if __name__ == "__main__":
    d = date(2023, 12, 1)
    print(d)
    print(date.today())
    print(d.strftime("%Y---%m---%d"))
    print(date.today() - d)
    print(type(date.today() - d))
