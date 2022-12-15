from datetime import date

from seminar.group_912.seminar_10.car import Car
from seminar.group_912.seminar_11.domain.client import Client
from seminar.group_912.seminar_11.domain.rental import Rental
from seminar.group_912.seminar_11.domain.rental_validators import RentalValidator
from seminar.group_912.seminar_11.repository.rental_repo import RentalRepository
from seminar.group_912.seminar_11.services.car_service import CarService


class RentalService:
    # To do its job, the RentalService needs the rental repo, a car service
    # and a way to validate car instances
    def __init__(self, repo: RentalRepository, car_service: CarService, rental_validator: RentalValidator):
        self._repo = repo
        self._car_service = car_service
        self._validator = rental_validator

    # We assume we read fields in the UI and create the object here
    def add(self, rental_id: int, start_date: date, end_date: date, client: Client, car: Car):
        # 1. Create the object
        rent = Rental(rental_id, start_date, end_date, client, car)
        # 2. Validate it -> exception if something is wrong
        self._validator.validate(rent)
        # 3. Add to rentals repo
        self._repo.add(rent)

    def statistic_cars_by_rental_days(self):
        pass
