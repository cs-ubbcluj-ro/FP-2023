from src2023.lecture.livecoding.lecture12.domain.exceptions import FlightAppException
from src2023.lecture.livecoding.lecture12.domain.flight import Flight
from src2023.lecture.livecoding.lecture12.domain.mytime import mytime
from src2023.lecture.livecoding.lecture12.repo.FligthRepo import FlightRepo
from src2023.lecture.livecoding.lecture12.services.flight_validator import FlightValidator


class UndoRedoError(FlightAppException):
    pass


class TimeInterval:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    @property
    def start(self) -> mytime:
        return self.__start

    @property
    def end(self) -> mytime:
        return self.__end

    def __str__(self):
        return f"{self.start} - {self.end}"


class Operation:
    """
    Class Operation acts as an abstract base class
    Note: we can use module abc
    """

    def undo(self):
        raise NotImplementedError()

    def redo(self):
        raise NotImplementedError()


class AddFlightOperation(Operation):
    def __init__(self, flight: Flight, repo: FlightRepo):
        self.__flight = flight
        self.__repo = repo

    def undo(self):
        self.__repo.remove(self.__flight.id)

    def redo(self):
        self.__repo.add(self.__flight)


class FlightService:
    def __init__(self, validator: FlightValidator, repo: FlightRepo):
        # NOTE Allows you to change validators at runtime
        self._validator = validator
        # NOTE Works with any class derived from FlightRepo
        self._repo = repo
        # History of program's operations
        self.__history = []
        self.__undo_index = -1

    def add_flight(self, flight: Flight):
        # TODO Some validations are internal to the flight object
        # NOTE Validation errors bounce back into the UI layer
        self._validator.validate(flight)
        # NOTE Repo does the unique id validation
        self._repo.add(flight)
        # Recording for undo/redo is the last step
        self.__history.append(AddFlightOperation(flight, self._repo))
        self.__undo_index = len(self.__history) - 1

    def undo(self):
        if self.__undo_index == -1:
            raise UndoRedoError("No more undos")
        self.__history[self.__undo_index].undo()
        self.__undo_index -= 1

    def get_all(self):
        return self._repo.get_all()

    def determine_longest_no_flight_intervals(self) -> []:
        result = []
        flights = self._repo.get_all()
        flights.sort(key=lambda x: x.dep_time)

        latest_arrival_time = mytime(0, 0)

        for flight in flights:
            if flight.dep_time > latest_arrival_time:
                result.append(TimeInterval(latest_arrival_time, flight.dep_time))

            if flight.arr_time > latest_arrival_time:
                latest_arrival_time = flight.arr_time

        result.sort(reverse=True, key=lambda x: x.end - x.start)
        return result

    def determine_maximum_number_of_backup_flights(self) -> [Flight]:
        result = []

        flights = self._repo.get_all()
        flights.sort(key=lambda x: x.arr_time)
        last_arrival_time = mytime(0, 0)

        for flight in flights:
            if flight.dep_time >= last_arrival_time:
                result.append(flight)
                last_arrival_time = flight.arr_time
        return result
