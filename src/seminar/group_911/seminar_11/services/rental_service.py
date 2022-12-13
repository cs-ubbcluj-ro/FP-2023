from datetime import date

from seminar.group_911.seminar_11.domain.car import Car
from seminar.group_911.seminar_11.domain.client import Client
from seminar.group_911.seminar_11.domain.rental import Rental
from seminar.group_911.seminar_11.repository.rental_repo import RentalRepository
from seminar.group_911.seminar_11.services.car_service import CarService


class CarsRentalsDTO:
    """
    Data transfer object for car rental statistic
    Holds the number of total rental days for one specific car
    """

    def __init__(self, car: Car, rental_days: int):
        self._car = car
        self._rental_days = rental_days

    @property
    def days(self):
        return self._rental_days

    @days.setter
    def days(self, new_value):
        self._rental_days = new_value

    def __repr__(self):
        return str(self.days) + " days for -> " + str(self._car)


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
        # let's print all cars
        cars = self._car_service.get_all()
        # print(cars)
        # let's print all rentals
        rentals = self._repo.get_all()
        # print(rentals)

        # NOTE license plates are keys, DTO instances are values
        rental_dict = {}

        for rental in self._repo.get_all():
            license_plate = rental.car.car_id
            if license_plate in rental_dict:
                rental_dict[license_plate].days += len(rental)
            else:
                rental_dict[license_plate] = CarsRentalsDTO(rental.car, len(rental))

        # move data from the {} to []
        result = list(rental_dict.values())
        result.sort(key=lambda x: x.days, reverse=True)

        return result
