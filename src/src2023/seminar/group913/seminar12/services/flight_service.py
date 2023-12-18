from src2023.seminar.group913.seminar12.domain.flight import Flight
from src2023.seminar.group913.seminar12.repo.FligthRepo import FlightRepo
from src2023.seminar.group913.seminar12.services.flight_validator import FlightValidator


class FlightService:
    def __init__(self, validator: FlightValidator, repo: FlightRepo):
        # NOTE Allows you to change validators at runtime
        self._validator = validator
        # NOTE Works with any class derived from FlightRepo
        self._repo = repo

    def add_flight(self, flight: Flight):
        # TODO Some validations are internal to the flight object
        # NOTE Validation errors bounce back into the UI layer
        self._validator.validate(flight)
        # NOTE Repo does the unique id validation
        self._repo.add(flight)
