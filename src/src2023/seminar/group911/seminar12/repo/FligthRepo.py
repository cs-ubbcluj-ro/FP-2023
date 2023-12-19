from src2023.seminar.group911.seminar12.domain.flight import Flight
from src2023.seminar.group911.seminar12.domain.mytime import mytime


class RepoError(Exception):
    pass


class FlightRepo:
    def __init__(self):
        # NOTE keys are flight.id, values are the flight objects
        self.__data = {}
        # NOTE We load all flight data when starting repo
        self.__load()

    def add(self, flight: Flight):
        fl = self.find(flight.id)

        if fl is not None:
            raise RepoError(f"Flight with id {fl.id} already exists!")

        # NOTE Check that 2 departures/landing do not happen at the same airport
        # in the same minute
        for f in self.__data.values():
            if flight.dep_city == f.dep_city:
                if flight.dep_time == f.dep_time:
                    raise RepoError("Flights " + f.id + " and " + flight.id + "  have same departure time and airport")
        # TODO Some more of these nice checks :)

        self.__data[flight.id] = flight
        self.__save()

    def remove(self, flight_id: str) -> Flight:
        """
        Remove the flight with given id from repository
        :param flight_id: The flight id
        :return: The deleted flight
        Raise RepoError if flight not found
        """
        flight = self.find(flight_id)

        if flight is None:
            raise RepoError(f"Flight with id {flight_id} does not exist!")

        fl = self.__data.pop(flight_id)
        self.__save()
        return fl

    def __load(self):
        with open("flights.txt", "r") as f:
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    continue
                (
                    flight_id,
                    dep_city,
                    dep_time,
                    arr_city,
                    arr_time,
                ) = line.split(",")

                dep_time_hm = dep_time.split(":")
                dep_time = mytime(int(dep_time_hm[0]), int(dep_time_hm[1]))
                arr_time_hm = arr_time.split(":")
                arr_time = mytime(int(arr_time_hm[0]), int(arr_time_hm[1]))

                flight = Flight(flight_id, dep_city, dep_time, arr_city, arr_time)

                self.__data[flight_id] = flight

    def __save(self):
        with open("flights.txt", "w") as f:
            for flight in self.__data.values():
                f.write(
                    f"{flight.id},{flight.dep_city},{flight.dep_time},{flight.arr_city},{flight.arr_time}\n"
                )

    def find(self, flight_id: str) -> Flight:
        """
        Search for the flight with the given id
        :param flight_id: The id of the flight
        :return: The flight object or None if it does not exist
        """
        if flight_id not in self.__data.keys():
            return None
        return self.__data[flight_id]

    # NOTE How to get objects from the repository!?
    # this would be get_all() some time ago
    # 1. Implement an iterator (__iter__, __next__)
    # 2. return a copy of the Flight objects ( -> it does not allow modufying the data)
    def get_all(self) -> [Flight]:
        # NOTE We return a shallow copy
        return list(self.__data.values())
