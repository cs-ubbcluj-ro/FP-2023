from datetime import date

from src2023.seminar.group914.seminar10.domain.car import Car
from src2023.seminar.group914.seminar10.domain.client import Client


class Rental:

    def __init__(self, id: str, car: Car, client: Client, start: date, end: date):
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
    print(date.today())
    d = date(2023, 11, 23)
    print(d)
    print(d.strftime("%Y/%m/%d"))
