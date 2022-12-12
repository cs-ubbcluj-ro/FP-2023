from datetime import date

from seminar.group_911.seminar_11.domain.car import Car
from seminar.group_911.seminar_11.domain.client import Client
from seminar.group_911.seminar_11.domain.rental import Rental
from seminar.group_911.seminar_11.repository.rental_repo import RentalRepository
from seminar.group_911.seminar_11.services.car_service import CarService


class RentalService:
    def __init__(self, repo: RentalRepository, car_service: CarService, validator):
        self._repo = repo
        # NOTE all *Service classes are the same layer so they can know about each other
        self._car_service = car_service
        self._validator = validator

    def add_rental(self, rental_start: date, rental_end: date, client: Client, car: Car):
        # 1. Build Rental instance
        # TODO rental ID!
        rent = Rental(100, rental_start, rental_end, client, car)
        # 2. Validate it
        self._validator.validate(rent)
        # 3. Add to repo
        self._repo.add(rent)

    #  The list of all cars in the car pool sorted by number of days they
    # were rented.
    def cars_sorted_by_rental_days(self):
        pass
