from archive.src_2022_2023.seminar.group_911.seminar_14.services.flights_service import FlightService


class UI:
    def __init__(self, service: FlightService):
        self.flightservice = service

    def RUN_PROGRAM(self):
        while (True):
            print("---MENU---\na. Display all flights\nx. Exit")
            input_key = input(">")

            if input_key.lower() in ["a", "x"]:
                self._runCommand(input_key.lower())

    def _runCommand(self, key):
        if (key == "a"):
            flight_list = self.flightservice.getAllFlights()
            for flight in flight_list:
                print(flight)
            print()

        elif (key == "x"):
            quit()
