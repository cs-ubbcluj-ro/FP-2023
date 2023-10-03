import unittest

from archive.src_2022_2023.seminar.group_911.seminar_14.repo.repo import FlightsRepo


class TestRepo(unittest.TestCase):
    def test_repo(self):
        repo = FlightsRepo("../flights.txt")
        self.assertEquals(len(repo), 22)
