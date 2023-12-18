from unittest import TestCase

from src2023.seminar.group913.seminar12.domain.flight import Flight
from src2023.seminar.group913.seminar12.domain.mytime import mytime
from src2023.seminar.group913.seminar12.services.flight_validator import FlightValidator, ValidationError


class TestFlightValidator(TestCase):
    def setUp(self):
        self._validator = FlightValidator()

    def test_validator(self):
        f = Flight("KL2710", "Timisoara", mytime(14, 25), "Bucuresti", mytime(15, 40))
        # NOTE Test that no exception is raised
        self.assertEqual(self._validator.validate(f), None)

        f = Flight("KL2710", "Timisoara", mytime(14, 25), "Bucuresti", mytime(14, 39))
        self.assertRaises(ValidationError, self._validator.validate, f)
