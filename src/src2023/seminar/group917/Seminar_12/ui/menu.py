from domain.mytime import MyTime, MyTime, TimeHandlingException
from repository.repo_exceptions import RepoExceptions
from service.flight_service import FlightController
from colorama import Fore, Style

from service.flight_validator import ValidationException


class OperationCancelledException(Exception):
    pass


class Console:
    def __init__(self, flight_controller: FlightController):
        self.__flight_controller = flight_controller

    def print_menu(self):
        print('P. Print all the flights')
        print('E. Exit')
        print('1. Add a flight')
        print('2. Add a delay to a flight')
        print('3. List airports in decreasing order of activity')
        print('4. List time intervals during which no flights take place in decreasing order of duration')
        print('5. Main radar down. Plan the flights accordingly.')

    def print_flight_list(self):
        print('------ALL flights--------')
        list_of_flights = self.__flight_controller.list_flights()
        for flight in list_of_flights:
            print(flight)  # calls __str__, not necessary to call it explicitly
            # print(flight.__str__())

    def __plan_when_radar_down_ui(self):
        print('------Flight plan if radar down-------')
        plan = self.__flight_controller.plan_when_radar_is_down()
        for flight in plan:
            # 05:45 | 06:40 | RO650 | Cluj - Bucuresti
            print(
                f"{flight.get_departure_time()} | {flight.get_arrival_time()} | {flight.get_flight_id()} | {flight.get_departure_city()} - {flight.get_destination_city()}")

    def __list_airports_by_activity_ui(self):
        print('----Airports by activity-----')
        airport_activity = self.__flight_controller.sort_by_activity()
        for airport_data in airport_activity:
            print(airport_data)

    def __list_no_flight_intervals_ui(self):
        print('-----Intervals with no flights------')
        result = self.__flight_controller.get_no_fly_intervals()
        for time_interval in result:
            print(time_interval)

    def __create_time_obj_from_str(self, time_str):
        dep_time_elements = time_str.split(':')
        if len(dep_time_elements) == 2:
            hour, minute = dep_time_elements[0], dep_time_elements[1]
            second = 0
        elif len(dep_time_elements) == 3:
            hour, minute, second = dep_time_elements[0], dep_time_elements[1], dep_time_elements[2]
        else:
            raise TimeHandlingException("Wrong input for time.")
        return MyTime(int(hour), int(minute), int(second))

    def __read_flight_data(self):
        flight_id = input('Flight id:')
        departure_city = input('Departure city:')
        departure_time = input('Departure time (format: HH:MM:SS):')
        destination_city = input('Destination city:')
        arrival_time = input('Arrival time (format: HH:MM:SS):')

        departure_time = self.__create_time_obj_from_str(departure_time)
        arrival_time = self.__create_time_obj_from_str(arrival_time)
        return flight_id, departure_city, departure_time, destination_city, arrival_time

    def __add_flight_ui(self):
        flight_data = self.__read_flight_data()
        flight_id, departure_city, departure_time, destination_city, arrival_time = flight_data

        self.__flight_controller.add_flight(flight_id, departure_city, departure_time, destination_city,
                                            arrival_time)

    def __modify_flight_ui(self):
        flight_id = input('ID of flight to be delayed:')
        delay = input('How many hours and minutes of delay (HH:MM):')

        delay = self.__create_time_obj_from_str(time_str=delay)
        old_flight = self.__flight_controller.modify_flight(flight_id, delay)
        print(Fore.GREEN + 'SUCCESS:' + Style.RESET_ALL + "Flight with id", flight_id, "was modified successfully.")

    def run(self):
        while True:
            self.print_menu()
            try:
                option = input(">>>").upper()
                match option:
                    case '1':
                        self.__add_flight_ui()
                    case '2':
                        self.__modify_flight_ui()
                    case '3':
                        self.__list_airports_by_activity_ui()
                    case '4':
                        self.__list_no_flight_intervals_ui()
                    case '5':
                        self.__plan_when_radar_down_ui()
                    case 'P':
                        self.print_flight_list()
                    case 'E':
                        return
            except OperationCancelledException:
                print("Operation cancelled. Back to the main menu")
            # NOTE With a common superclass called FlightAppException
            except ValidationException as ve:
                print(Fore.MAGENTA + 'Validation exception(s):' + str(ve) + Style.RESET_ALL)
            except RepoExceptions as re:
                print(Fore.RED + 'Repository exception(s):' + str(re) + Style.RESET_ALL)
            except TimeHandlingException as te:
                print(Fore.BLUE + 'Time-related exception:' + str(te) + Style.RESET_ALL)
