from time import struct_time, strftime, strptime


class Flight():
    def __init__(self, id: str, departure: str, departure_time: struct_time, arrival: str, arrival_time: struct_time):
        self.__id = id
        self.__departure = departure
        self.__departure_time = departure_time
        self.__arrival = arrival
        self.__arrival_time = arrival_time

    @property
    def id(self):
        return self.__id

    @property
    def departure(self):
        return self.__departure

    @property
    def departure_time(self):
        return self.__departure_time

    @property
    def arrival(self):
        return self.__arrival

    @property
    def arrival_time(self):
        return self.__arrival_time

    def __str__(self):
        # return f"Flight {self.__id} from {self.__departure} at {self.__departure_time} to {self.__arrival} at {self.__arrival_time}."
        return repr(self)

    def __repr__(self):
        dep_time = strftime("%H:%M", self.departure_time)
        arr_time = strftime("%H:%M", self.arrival_time)
        return dep_time + " | " + arr_time + " | " + self.id + " | " + self.departure + " - " + self.arrival
        # return f"Flight({self.__id},'{self.__departure}','{dep_time}','{self.__arrival}','{arr_time}')"
