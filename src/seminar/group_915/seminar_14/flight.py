from datetime import time
from time import strptime, strftime


class Flight:
    def __init__(self, id: str, departure_city: str, departure_time: time, arrival_city: str, arrival_time: time):
        self._id = id
        self._departure_city = departure_city
        self._departure_time = departure_time
        self._arrival_city = arrival_city
        self._arrival_time = arrival_time

    @property
    def id(self):
        return self._id

    @property
    def departure_city(self):
        return self._departure_city

    @departure_city.setter
    def departure_city(self, city: str):
        self._departure_city = city

    @property
    def departure_time(self):
        return self._departure_time

    @departure_time.setter
    def departure_time(self, time: time):
        self._departure_time = time

    @property
    def arrival_city(self):
        return self._arrival_city

    @arrival_city.setter
    def arrival_city(self, city: str):
        self._arrival_city = city

    @property
    def arrival_time(self):
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, time: time):
        self._arrival_time = time

    def __str__(self):
        return f"Flight {self._id}, departure in {self._departure_city} at {self._departure_time}, arrival in {self._arrival_city} at {self._departure_time}"
