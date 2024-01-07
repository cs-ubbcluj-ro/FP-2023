from domain.flight import Flight
from domain.mytime import MyTime
from repository.repo_exceptions import RepoFileNotFoundException, RepoExceptions, FlightNotFoundException
import os


# Ujfalusi Abel
class FlightRepo:
    def __init__(self, file_path="data/flights.txt"):
        self.__flights = {}
        self.__file_path = file_path
        self.__load_from_file()

    #Tiut Cristian
    def add_flight(self, flight_to_add: Flight):
        """
        Adds a flight_to_add to the repo
        :param flight_to_add: flight_to_add to be added
        :post_cond: flight_to_add was added to the repo
        """
        if flight_to_add.get_flight_id() in self.__flights:
            raise RepoExceptions("Flight with this ID already exists.")
        # TO-DO: make these comparisons prettier (and maybe easier to understand)
        for flight_from_list in self.__flights.values():
            if flight_to_add.get_departure_city() == flight_from_list.get_departure_city() and flight_to_add.get_departure_time() == flight_from_list.get_departure_time():
                raise RepoExceptions("There's already a flight_to_add with same departure city and time.")
            if flight_to_add.get_departure_city() == flight_from_list.get_destination_city() and flight_to_add.get_departure_time() == flight_from_list.get_arrival_time():
                raise RepoExceptions(
                    "There exists a flight_to_add that arrives in " + flight_to_add.get_departure_city() + " at " + str(
                        flight_to_add.get_departure_time()))
            if flight_to_add.get_destination_city() == flight_from_list.get_destination_city() and flight_to_add.get_arrival_time() == flight_from_list.get_arrival_time():
                raise RepoExceptions("There's already a flight_to_add with same destination city and time.")

            if flight_to_add.get_destination_city() == flight_from_list.get_departure_city() and flight_to_add.get_arrival_time() == flight_from_list.get_departure_time():
                raise RepoExceptions(
                    "There exists a flight_to_add that departs from " + flight_to_add.get_destination_city() + " at " + str(
                        flight_to_add.get_arrival_time()))

        self.__flights[flight_to_add.get_flight_id()] = flight_to_add
        self.__save_to_file()

    def find_flight(self, flight_id):
        if flight_id in self.__flights:
            return self.__flights[flight_id]
        raise FlightNotFoundException(flight_id)

    def update_flight(self, flight_id, modified_flight):
        # Q: How else could we have implemented update/modification?
        flight = self.find_flight(flight_id)
        self.__flights[flight_id] = modified_flight
        self.__save_to_file()
        return flight

    def __load_from_file(self):
        if not os.path.isfile(self.__file_path):
            raise RepoFileNotFoundException(self.__file_path)
        with open(self.__file_path, "r", encoding="UTF-8") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                # SLD322,Timisoara,09:05:00,Cluj,10:00:00
                try:
                    flight_id, departure_city, departure_time, arrival_city, arrival_time = line.split(",")
                    dep_hour, dep_mins, dep_secs = departure_time.split(':')
                    departure_time = MyTime(int(dep_hour), int(dep_mins), int(dep_secs))
                    arr_hour, arr_mins, arr_secs = arrival_time.split(':')

                    arrival_time = MyTime(int(arr_hour), int(arr_mins), int(arr_secs))
                    flight = Flight(flight_id, departure_city, departure_time, arrival_city, arrival_time)
                    self.__flights[flight_id] = flight
                except:
                    raise RepoExceptions(
                        "Something went wrong while reading from file (either not enough fields, or time in incorrect format).")

    def __save_to_file(self):
        if not os.path.isfile(self.__file_path):
            raise RepoFileNotFoundException(self.__file_path)
        with open(self.__file_path, "w", encoding="UTF-8") as file:
            for flight in self.__flights.values():
                line = ','.join([flight.get_flight_id(), flight.get_departure_city(), str(flight.get_departure_time()),
                                 flight.get_destination_city(), str(flight.get_arrival_time())])
                line += '\n'
                file.write(line)

    def list_flights(self):
        return list(self.__flights.values())
