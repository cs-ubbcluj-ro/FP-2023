from collections import defaultdict

from domain.flight import Flight
from domain.mytime import MyTime
from repository.flight_repo import FlightRepo
from service.flight_validator import FlightValidator


class AirportData:
    def __init__(self, location, activity):
        self.__airport_location = location
        self.__activity = activity

    @property
    def location(self):
        return self.__airport_location

    @location.setter
    def location(self, new_location):
        self.__airport_location = new_location

    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, new_activity):
        self.__activity = new_activity

    def add_activity(self):
        self.__activity += 1

    def __str__(self):
        return "Location: " + self.location + ' | Number of flights: ' + str(self.activity)


class TimeInterval:
    def __init__(self, start: MyTime, end: MyTime):
        self.__start = start
        self.__end = end

    @property
    def start_time(self):
        return self.__start

    @property
    def end_time(self):
        return self.__end

    @start_time.setter
    def start_time(self, new_st):
        self.__start = new_st

    @end_time.setter
    def end_time(self, new_end):
        self.__end = new_end

    @property
    def duration(self):
        difference = self.__end - self.__start
        return difference
        # return difference.hour * 60 + difference.minute

    def __str__(self):
        return "Time Interval: " + str(self.start_time) + '->' + str(self.end_time) + ' with duration: ' + str(
            self.duration)


class FlightController:
    def __init__(self, flight_repo, flight_validator: FlightValidator):
        self.__flight_repo = flight_repo
        self.__flight_validator = flight_validator

    def list_flights(self):
        return self.__flight_repo.list_flights()

    def add_flight(self, flight_id, departure_city, departure_time, destination_city, arrival_time):
        flight = Flight(flight_id, departure_city, departure_time, destination_city, arrival_time)
        self.__flight_validator.validate(flight)
        self.__flight_repo.add_flight(flight)

    def modify_flight(self, flight_id, delay):
        #validations for delay? Set limits to possible delay?
        #Are we guaranteed to get a valid flight after adding delay?
        flight = self.__flight_repo.find_flight(flight_id)
        new_departure_time = flight.get_departure_time() + delay
        new_arrival_time = flight.get_arrival_time() + delay
        new_flight = Flight(flight_id, flight.get_departure_city(), new_departure_time, flight.get_destination_city(),
                            new_arrival_time)
        return self.__flight_repo.update_flight(flight_id, new_flight)

    def sort_by_activity(self):
        flights = self.list_flights()
        location_activity = defaultdict(int)
        for flight in flights:
            location_activity[flight.get_departure_city()] += 1
            location_activity[flight.get_destination_city()] += 1

        airport_activity_items = location_activity.items()
        # could just sort this list of tuples and return it
        airport_activity_items = [AirportData(location, activity) for location, activity in airport_activity_items]
        airport_activity_items.sort(key=lambda airport: airport.activity, reverse=True)
        return airport_activity_items

    def get_no_fly_intervals(self):
        time_intervals = []
        flights = self.__flight_repo.list_flights()

        flights.sort(key=lambda x: x.get_departure_time())

        latest_arrival_time = MyTime(0, 0)

        for flight in flights:
            print(flight)
            if flight.get_departure_time() > latest_arrival_time:
                # if time passed between the last arrival time we recorded
                # and the current flight (remember, the flight list we are
                # working on is sorted by departure time) it means we have a new
                # interval with no flights
                time_intervals.append(TimeInterval(latest_arrival_time, flight.get_departure_time()))

            # modify latest arrival time with the current one (if it's later
            # than what we have recorded
            # Q: why don't we do this in the previous if?
            if flight.get_arrival_time() > latest_arrival_time:
                latest_arrival_time = flight.get_arrival_time()
            # print('Latest arrival time',latest_arrival_time)

        day_finish = MyTime(23, 59)
        if latest_arrival_time < day_finish:
            time_intervals.append(TimeInterval(latest_arrival_time, day_finish))

        time_intervals.sort(reverse=True, key=lambda x: x.duration)
        return time_intervals

    def plan_when_radar_is_down(self):
        #This is the classic activity scheduling problem formulated with flights
        flights = self.__flight_repo.list_flights()
        flights.sort(key=lambda flight: flight.get_arrival_time())

        plan = []
        last_arrival_time = MyTime(0, 0)
        for flight in flights:
            if flight.get_departure_time() > last_arrival_time:
                plan.append(flight)
                last_arrival_time = flight.get_arrival_time()
        return plan
