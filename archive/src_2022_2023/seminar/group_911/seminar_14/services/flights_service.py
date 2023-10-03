from archive.src_2022_2023.seminar.group_911.seminar_14.repo.repo import FlightsRepo


class FlightService:
    def __init__(self, repo: FlightsRepo):
        self._flightrepository = repo

    def getAllFlights(self):
        return list(self._flightrepository.get_all())

    def addFlight(self, params):
        pass
