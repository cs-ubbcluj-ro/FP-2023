from unittest import TestCase
from datetime import time

from src2023.seminar.group913.seminar12.domain.flight import Flight
from src2023.seminar.group913.seminar12.domain.mytime import mytime


class FlightTest(TestCase):
    def setUp(self):
        self._f = Flight("KL2710", "Timisoara", mytime(14, 25), "Bucuresti", mytime(15, 40))

    def test_flight(self):
        self.assertEqual(self._f.id, "KL2710")
        self.assertEqual(self._f.dep_city, "Timisoara")
        # NOTE datetime.time class should implement __eq__ for this
        self.assertEqual(self._f.dep_time, mytime(14, 25))
        self.assertEqual(self._f.arr_city, "Bucuresti")
        self.assertEqual(self._f.arr_time, mytime(15, 40))
