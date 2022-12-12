from datetime import date

from seminar.group_911.seminar_11.domain.car import Car
from seminar.group_911.seminar_11.domain.client import Client


class Rental:
    def __init__(self, rental_id: int, start: date, end: date, client: Client, car: Car):
        self._rentalId = rental_id
        self._client = client
        self._car = car
        self._start = start
        self._end = end

    @property
    def id(self):
        return self._rentalId

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, car):
        self._car = car

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        self._end = end

    # len(rental)
    def __len__(self):
        if self._end is not None:
            return (self._end - self._start).days + 1
        today = date.today()
        return (today - self._start).days + 1

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Rental: " + str(self.id) + "\nCar: " + str(self.car) + "\nClient: " + str(
            self.client) + "\nPeriod: " + self._start.strftime("%Y-%m-%d") + " to " + self._end.strftime("%Y-%m-%d")


if __name__ == "__main__":
    car = Car("CJ 01 ABC", "Dacia", "Sandero", "red")
    client = Client(100, "280122334506070", "Pop Maria")

    r = Rental(100, date(2022, 10, 15), date(2022, 11, 20), client, car)
    print(len(r))

    r = Rental(100, date(2022, 10, 15), None, client, car)
    print(len(r))
