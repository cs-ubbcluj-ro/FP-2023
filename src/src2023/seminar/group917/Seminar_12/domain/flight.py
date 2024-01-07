from domain.mytime import MyTime, MyTime


class Flight:
    def __init__(self, flight_id: str, departure_city: str, departure_time: MyTime, destination_city: str,
                 arrival_time: MyTime):
        self.__flight_id = flight_id
        self.__departure_city = departure_city
        self.__departure_time = departure_time
        self.__destination_city = destination_city
        self.__arrival_time = arrival_time

    #Can use @property/setter instead of get_, set_ methods
    def get_flight_id(self):
        return self.__flight_id

    def get_departure_city(self):
        return self.__departure_city

    def set_departure_city(self, city):
        self.__departure_city = city

    def get_destination_city(self):
        return self.__destination_city

    def set_destination_city(self, city):
        self.__destination_city = city

    def get_departure_time(self):
        return self.__departure_time

    def set_departure_time(self, departure_time):
        self.__departure_time = departure_time

    def get_arrival_time(self):
        return self.__arrival_time

    def set_arrival_time(self, arrival_time):
        self.__arrival_time = arrival_time

    def get_duration(self):
        return self.__arrival_time - self.__departure_time

    def __str__(self):
        return (self.__flight_id + ","
                + self.__departure_city + ","
                + str(self.__departure_time) + ","
                + self.__destination_city + ","
                + str(self.__arrival_time))


# f1 = Flight('TAR9372', 'Bucuresti', MyTime(10,15,0), 'Madrid', MyTime(12,5,10))
# f2 = Flight('WIZZ947', 'Cluj', MyTime(9,55,0), 'Basel', MyTime(11,35,0))
#
# print(f1.get_duration())
# print(f2.get_duration())
