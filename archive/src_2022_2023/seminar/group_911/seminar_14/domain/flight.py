# Butnar Dragos-Mihai
import datetime
import time


class Flight:
    def __init__(self, f_id: str, depart_city: str, dtime: time.struct_time, arrival_city: str,
                 atime: time.struct_time):
        self.__id = f_id
        self.__depart = depart_city
        self.__dtime = dtime
        self.__arrive = arrival_city
        self.__atime = atime

    @property
    def id(self):
        return self.__id

    @property
    def departure_city(self):
        return self.__depart

    @property
    def arrival_city(self):
        return self.__arrive

    @property
    def departure_time(self):
        return self.__dtime

    @property
    def arrival_time(self):
        return self.__atime

    def __str__(self):
        dtime = time.strftime("%H:%M", self.departure_time)
        atime = time.strftime("%H:%M", self.arrival_time)
        return f"{self.id},{self.departure_city},{dtime},{self.arrival_city},{atime}\n"
