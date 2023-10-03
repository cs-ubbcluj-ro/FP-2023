# Timoce Darius
class Flight:
    def __init__(self, identifier: str, departure_city: str, departure_time: str, arrival_city: str, arrival_time: str):
        self.__identifier = identifier
        self.__departure_city = departure_city
        self.__departure_time = departure_time
        self.__arrival_city = arrival_city
        self.__arrival_time = arrival_time

    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, new_identifier: str):
        self.__identifier = new_identifier

    @property
    def departure_city(self):
        return self.__departure_city

    @departure_city.setter
    def departure_city(self, new_departure_city: str):
        self.__departure_city = new_departure_city

    @property
    def departure_time(self):
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, new_departure_time: str):
        self.__departure_time = new_departure_time

    @property
    def arrival_city(self):
        return self.__arrival_city

    @arrival_city.setter
    def arrival_city(self, new_arrival_city):
        self.__arrival_city = new_arrival_city

    @property
    def arrival_time(self):
        return self.__arrival_time

    @arrival_time.setter
    def arrival_time(self, new_arrival_time):
        self.__arrival_city = new_arrival_time

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.__identifier + "," + self.departure_city + "," + self.__departure_time + "," + self.__arrival_city + "," + self.__arrival_time
