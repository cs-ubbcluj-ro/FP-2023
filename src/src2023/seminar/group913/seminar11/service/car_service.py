from src2023.seminar.group913.seminar11.domain.car import Car
from src2023.seminar.group913.seminar11.service.undo_service import FunctionCall, Operation


class CarService:
    def __init__(self, undo_service, rental_service, validator, repository):
        self._validator = validator
        self._repository = repository
        self._rental_service = rental_service
        self._undo_service = undo_service

    def create(self, car_id, license_plate, car_make, car_model):
        car = Car(car_id, license_plate, car_make, car_model)
        self._validator.validate(car)
        self._repository.store(car)
        return car

    def delete(self, car_id):
        """
            1. Delete the car from the repository
        """
        car = self._repository.delete(car_id)

        """
        Record car deletion for undo/redo
        """
        fredo = FunctionCall(self._repository.delete, car_id)
        fundo = FunctionCall(self._repository.store, car)
        self._undo_service.record(Operation(fundo, fredo))


        '''
            2. Delete its rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        rentals = self._rental_service.filter_rentals(None, car)
        for rent in rentals:
            self._rental_service.delete_rental(rent.id)
        return car

    def update(self, car):
        """
            NB! Undo/redo is also needed here
        """
        # TODO Implement later...
        pass
