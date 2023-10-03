from archive.src_2022_2023.seminar.group_915.seminar_14.flights_repo import TextFlightRepository


class FlightsServices:
    def __init__(self, repo: TextFlightRepository):
        self._repo = repo

    def get_all(self):
        return self._repo.get_all()
