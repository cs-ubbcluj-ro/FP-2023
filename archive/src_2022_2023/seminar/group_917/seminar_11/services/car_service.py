from archive.src_2022_2023.seminar.group_917.seminar_11.domain.car import car
from archive.src_2022_2023.seminar.group_917.seminar_11.domain.car_validators import CarValidatorRO
from archive.src_2022_2023.seminar.group_917.seminar_11.repository import car_repo


class CarService:
    def __init__(self, repo: car_repo, car_validator: CarValidatorRO):
        self._repo = repo
        self._validator = car_validator

    def add_car(self, license_plate, make, model, color):
        # NOTE We expect this to be called from the UI in a completed program
        # 1. Build the car instance
        new_car = car(license_plate, make, model, color)
        # 2. Valdiate it
        self._validator.validate(new_car)
        # 3. Add it to repository
        self._repo.add(new_car)

    def get_all(self):
        # cheat method to return all cars :)
        # TODO implement a proper filter for cars (by make, model etc.)
        return self._repo.get_all()
