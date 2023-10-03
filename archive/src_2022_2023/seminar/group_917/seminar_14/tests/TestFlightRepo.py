import unittest

from archive.src_2022_2023.seminar.group_917.seminar_14.repo.flight_repo import FlightRepository


class TestFlightRepo(unittest.TestCase):
    def test_flight_repo(self):
        repo = FlightRepository("../flights.txt")
        self.assertEquals(22, len(repo))
