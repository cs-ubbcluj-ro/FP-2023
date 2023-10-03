from archive.src_2022_2023.seminar.group_917.seminar_14.repo.flight_repo import FlightRepository


class FlightServices:
    def __init__(self, flightRepository: FlightRepository):
        self._flightRepository = flightRepository

    def get_all(self):
        return self._flightRepository.get_all()

    # Turcu Mihnea
