from datetime import time
from unittest import TestCase

from src2023.seminar.group914.seminar12.domain.flight import Flight


class FlightRepoTest(TestCase):
    def setUp(self):
        self._f = Flight("KL2710", "Timisoara", time(14, 25), "Bucuresti", time(15, 40))

    def test_repo(self):
        pass
