class Flight_services():
    def __init__(self, repo):
        self.__repo = repo

    def get_all(self):
        result = ''
        for flight in self.__repo.get_all():
            result += str(flight)
            result += '\n'
        return result

    def add_flight(self, id, departure, departure_time, arrival, arrival_time):
        # TODO FlightValidator.validate(...)
        self.__repo.add_flight(id, departure, departure_time, arrival, arrival_time)
