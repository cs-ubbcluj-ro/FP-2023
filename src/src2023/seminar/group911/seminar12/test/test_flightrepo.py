from datetime import time
from unittest import TestCase

from src2023.seminar.group911.seminar12.domain.flight import Flight
from src2023.seminar.group911.seminar12.repo.FligthRepo import RepoError, FlightRepo


class FlightRepoTest(TestCase):
    def setUp(self):
        self._repo = FlightRepo()

    def test_repo(self):
        self.assertEqual(len(self._repo.get_all()), 22)
        self.assertEqual(self._repo.find("RO650").dep_city, "Cluj")
        self.assertEqual(self._repo.find("RO650").arr_city, "Bucuresti")
        self.assertEqual(self._repo.find("RO650").dep_time, time(5, 45))
        self.assertEqual(self._repo.find("RO650").arr_time, time(6, 40))

        self.assertEqual(self._repo.find("RO734").dep_city, "Timisoara")
        self.assertEqual(self._repo.find("RO734").arr_city, "Iasi")
        self.assertEqual(self._repo.find("RO734").dep_time, time(10, 45))
        self.assertEqual(self._repo.find("RO734").arr_time, time(12, 25))

        self.assertEqual(self._repo.find("RO745").dep_city, "Cluj")
        self.assertEqual(self._repo.find("RO745").arr_city, "Iasi")
        self.assertEqual(self._repo.find("RO745").dep_time, time(12, 50))
        self.assertEqual(self._repo.find("RO745").arr_time, time(14, 5))

        self._repo.add(Flight("RO999", "Cluj", time(12, 50), "Iasi", time(14, 5)))
        self.assertEqual(len(self._repo.get_all()), 23)
        self.assertEqual(self._repo.find("RO999").dep_city, "Cluj")
        self.assertEqual(self._repo.find("RO999").arr_city, "Iasi")
        self.assertEqual(self._repo.find("RO999").dep_time, time(12, 50))
        self.assertEqual(self._repo.find("RO999").arr_time, time(14, 5))

        self.assertRaises(RepoError, self._repo.add, Flight("RO999", "Cluj", time(12, 50), "Iasi", time(14, 5)))
        self.assertRaises(RepoError, self._repo.add, Flight("RO999", "Bucuresti", time(11, 20), "Brasov", time(15, 5)))

        self._repo.remove("RO999")
        self.assertEqual(len(self._repo.get_all()), 22)
        self.assertEqual(self._repo.find("RO999"), None)

        self.assertRaises(RepoError, self._repo.remove, "RO999")
