from archive.src_2022_2023.seminar.group_912.seminar_14.domain.flight import Flight
from time import strptime


class TextFileRepository:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__flights = []
        self.__load_from_file()

    def add_flight(self, flight_number, departing_city, departing_time, arriving_city, arriving_time):
        self.__load_from_file()
        self.__flights.append(Flight(flight_number, departing_city, departing_time, arriving_city, arriving_time))
        # self.__store_to_file()

    def get_all_flights(self):
        self.__load_from_file()
        return self.__flights

    # def __store_to_file(self):
    #     f = open(self.__file_name, "w")
    #     for e in self.__flights:
    #         ex_str = str(Flight.get_flight_number(e)) + "," + str(Flight.get_departing_city(e)) + "," + str(
    #             Flight.get_departing_time(e)) + "," + str(Flight.get_arriving_city(e)) + "," + str(
    #             Flight.get_arriving_time(e)) + "\n"
    #         f.write(ex_str)
    #     f.close()

    def __load_from_file(self):
        self.__flights.clear()  # = []
        try:
            f = open(self.__file_name, "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(",")
                self.__flights.append(
                    Flight(line[0], line[1], strptime(line[2], "%H:%M"), line[3], strptime(line[4], "%H:%M")))
                line = f.readline().strip()
            f.close()
        except IOError as e:
            raise e


class AirportActivityDTO:
    def __init__(self, airport: str, activity: int):
        self._airport = airport
        self._activity = activity

    @property
    def airport(self):
        return self._airport

    @property
    def activity(self):
        return self._activity

    def __str__(self):
        return self.airport + " -> " + str(self.activity)


if __name__ == "__main__":
    repo = TextFileRepository("../flights.txt")

    for flight in repo.get_all_flights():
        print(flight)

    # NOTE Functionality 4 -> Services + DTO
    airports = dict()  # {}
    for f in repo.get_all_flights():
        if f.departure in airports:
            airports[f.departure] += 1
        else:
            airports[f.departure] = 1
        if f.arrival in airports:
            airports[f.arrival] += 1
        else:
            airports[f.arrival] = 1
    # dict -> list, sort descending
    airports_list = list()
    for item in airports:
        airports_list.append(AirportActivityDTO(item, airports[item]))
    airports_list.sort(reverse=True, key=lambda x: x.activity)
    for airport in airports_list:
        print(airport)
