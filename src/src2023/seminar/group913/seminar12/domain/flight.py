from datetime import time


class Flight:
    def __init__(self, flight_id: str, dep_city: str, dep_time: time, arr_city: str, arr_time: time):
        if not isinstance(flight_id, str):
            raise TypeError("Flight id must be an str")
        if not isinstance(dep_city, str):
            raise TypeError("Departure city must be an str")
        if not isinstance(arr_city, str):
            raise TypeError("Arrival city must be an str")
        if not isinstance(dep_time, time) or not isinstance(arr_time, time):
            raise TypeError("Departure/arrival times must be time instances")
        self.__id = flight_id
        self.__dep_city = dep_city
        self.__dep_time = dep_time
        self.__arr_city = arr_city
        self.__arr_time = arr_time

    @property
    def id(self):
        return self.__id

    @property
    def dep_city(self):
        return self.__dep_city

    @property
    def dep_time(self):
        return self.__dep_time

    @property
    def arr_city(self):
        return self.__arr_city

    @property
    def arr_time(self):
        return self.__arr_time

    def __str__(self):
        return "Flight " + self.id + " departs from " + self.dep_city + " at " + self.dep_time + ", arrives at " + self.arr_city + " at " + self.arr_time
