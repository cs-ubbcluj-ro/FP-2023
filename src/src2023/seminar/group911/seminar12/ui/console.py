from src2023.seminar.group911.seminar12.domain.flight import Flight
from src2023.seminar.group911.seminar12.domain.mytime import mytime
from src2023.seminar.group911.seminar12.repo.FligthRepo import RepoError
from src2023.seminar.group911.seminar12.services.flight_service import FlightService
from src2023.seminar.group911.seminar12.services.flight_validator import ValidationError


class OperationCancelled(Exception):
    pass


class UI:
    def __init__(self, flight_service: FlightService):
        self.__service = flight_service

    def __print_menu(self):
        print("Flight menu:")
        print("1. Add flight")
        print("2. Show flights")
        print("0. Exit")

    def __input(self, message):
        value = input(message)
        if value.upper() == 'XXX':
            raise OperationCancelled()
        return value

    def __read_time(self, input_message):
        try:
            flight_dep_time = self.__input(input_message)
            hour, minute = flight_dep_time.split(":")
            return mytime(int(hour), int(minute))
        except ValueError:
            print("Incorrect string for time")
            return None

    def __read_flight(self):
        print("Adding a new flight")
        print("(XXX to exit to main menu)")

        flight_id = ""
        while len(flight_id) < 1:
            flight_id = self.__input("Id: ")

        flight_dep_city = ""
        while len(flight_dep_city) < 1:
            flight_dep_city = self.__input("Departure city: ")

        flight_dep_time = None
        while flight_dep_time is None:
            flight_dep_time = self.__read_time("Departure time (hh:mm): ")

        flight_arr_city = ""
        while len(flight_arr_city) < 1:
            flight_arr_city = self.__input("Arrival city: ")

        flight_arr_time = None
        while flight_arr_time is None:
            flight_arr_time = self.__read_time("Arrival time (hh:mm): ")

        return Flight(flight_id, flight_dep_city, flight_dep_time, flight_arr_city, flight_arr_time)

    def __add_flight(self):
        flight = None
        while flight is None:
            try:
                flight = self.__read_flight()
                self.__service.add_flight(flight)
            except ValidationError as ve:
                flight = None
                print(ve)

    def __display_flights(self):
        print("-= All flights =-")
        for flight in self.__service.get_all():
            print(flight)

    def start(self):
        while True:
            try:
                self.__print_menu()
                opt = input(">>")

                if opt == "1":
                    self.__add_flight()
                elif opt == "2":
                    self.__display_flights()
                elif opt == "0":
                    print("Goodbye")
                    return
                else:
                    print("Invalid menu choice")
            except OperationCancelled:
                print("Operation cancelled. Back to the main menu")
            # NOTE With a common superclass called FlightAppException
            except (ValidationError, RepoError) as ve:
                print(ve)
