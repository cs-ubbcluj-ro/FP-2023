from src2023.seminar.group914.seminar12.domain.flight import Flight


class RepoError(Exception):
    pass


class FlightRepo:
    def __init__(self):
        # NOTE keys are flight.id, values are the flight objects
        self.__data = {}
        # NOTE We load all flight data when starting repo
        self.__load()

    def add(self, flight: Flight):
        # ...
        self.__save()

    def remove(self, flight_id: str) -> Flight:
        """
        Remove the flight with given id from repository
        :param flight_id: The flight id
        :return: The deleted flight
        Raise RepoError if flight not found
        """
        # ...
        self.__save()

    def __load(self):
        # TODO implement
        pass

    def __save(self):
        # TODO implement
        pass

    def find(self, flight_id: str) -> Flight:
        """
        Search for the flight with the given id
        :param flight_id: The id of the flight
        :return: The flight object or None if it does not exist
        """
        # try:
        #     return self.__data[flight_id]
        # except KeyError:
        #     return None
        # NOTE - Let's avoid creating an exception object
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
