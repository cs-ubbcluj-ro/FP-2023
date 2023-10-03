from archive.src_2022_2023.seminar.group_915.seminar_14.flights_repo import TextFlightRepository
from archive.src_2022_2023.seminar.group_915.seminar_14.flights_services import FlightsServices


class FlightsUI:
    def __init__(self, flight_service: FlightsServices):
        self._flight_service = flight_service

    def display_all_flights(self):
        flights = self._flight_service.get_all()
        for flight in flights:
            print(flight)

    def main_menu(self):
        while True:
            print("1. Display all flights")
            print("2. Exit")
            command = input(">> ")
            if command == "1":
                self.display_all_flights()
            elif command == "2":
                return
            else:
                print("Invalid command")


if __name__ == "__main__":
    repo = TextFlightRepository("flights.txt")
    services = FlightsServices(repo)
    ui = FlightsUI(services)
    ui.main_menu()
