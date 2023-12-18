from src2023.seminar.group913.seminar12.services.flight_service import FlightService


class UI:
    def __init__(self, flight_service: FlightService):
        self.__service = flight_service

    def __print_menu(self):
        print("Flight menu:")
        print("1. Add flight")
        print("2. Show flights")
        print("0. Exit")

    def __display_flights(self):
        print("-= All flights =-")
        for flight in self.__service.get_all():
            print(flight)

    def start(self):
        while True:
            self.__print_menu()
            opt = input(">>")

            if opt == "1":
                pass
            elif opt == "2":
                self.__display_flights()
            elif opt == "0":
                print("Goodbye")
                return
            else:
                print("Invalid menu choice")
