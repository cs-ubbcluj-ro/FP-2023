from datetime import date

from archive.src_2022_2023.seminar.group_912.seminar_10.car import Car
from archive.src_2022_2023.seminar.group_912.seminar_11.domain.client import Client
from archive.src_2022_2023.seminar.group_912.seminar_11.domain.rental import Rental
from archive.src_2022_2023.seminar.group_912.seminar_11.domain.rental_validators import RentalValidator
from archive.src_2022_2023.seminar.group_912.seminar_11.repository.rental_repo import RentalRepository
from archive.src_2022_2023.seminar.group_912.seminar_11.services.car_service import CarService


class CarRentalDaysDTO:
    # Data Transfer Object between service and UI layer
    def __init__(self, car, rental_days):
        self._car = car
        self._rental_days = rental_days

    @property
    def car(self):
        return self._car

    @property
    def days(self):
        return self._rental_days

    def __le__(self):
        # NOTE for sorting
        pass

    def __str__(self):
        return str(self.days) + " for car " + str(self.car)


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
        # NOTE keys are car license plates, values are total rental days
        rental_dict = {}

        for rental in self._repo.get_all():
            if rental.car.car_id not in rental_dict:
                rental_dict[rental.car.car_id] = len(rental)
            else:
                rental_dict[rental.car.car_id] += len(rental)

        # TODO add all cars that were never rented
        result = []
        for key in rental_dict:
            car = self._car_service.get(key)
            result.append(CarRentalDaysDTO(car, rental_dict[key]))

        # sort by number of rental days
        result.sort(key=lambda x: x.days, reverse=True)
        return result
