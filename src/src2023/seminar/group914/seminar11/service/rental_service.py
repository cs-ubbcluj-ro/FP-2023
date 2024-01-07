from src2023.seminar.group914.seminar11.domain.rental import Rental
from src2023.seminar.group914.seminar11.service.car_rental_exception import CarRentalException


class RentalService:
    """
    Service for rental operations
    """

    def __init__(self, undo_service, validator, rental_repo, car_repo, client_repo):
        self._validator = validator
        self._carRepo = car_repo
        self._cliRepo = client_repo
        self._repository = rental_repo

        self._undoController = undo_service

    def create_rental(self, rental_id, client, car, start, end):
        rental = Rental(rental_id, start, end, client, car)
        self._validator.validate(rental)

        '''
        Check the car's availability for the given period 
        '''
        if self.is_car_available(rental.car, rental.start, rental.end) is False:
            raise CarRentalException("Car is not available during that time!")

        self._repository.store(rental)
        return rental

    def is_car_available(self, car, start, end):
        """
        Check the availability of the given car to be rented in the provided time period
        car - The availability of this car is verified
        start, end - The time span. The car is available if it is not rented in this time span
        Return True if the car is available, False otherwise
        """
        rentals = self.filter_rentals(None, car)
        for rent in rentals:
            if start > rent.end or end < rent.start:
                continue
            return False
        return True

    def filter_rentals(self, client, car):
        """
        Return a list of rentals performed by the provided client for the provided car
        client - The client performing the rental. None means all clients
        cars - The rented car. None means all cars 
        """
        result = []
        for rental in self._repository.get_all():
            if client is not None and rental.client != client:
                continue
            if car is not None and rental.car != car:
                continue
            result.append(rental)
        return result

    def delete_rental(self, rental_id):
        rental = self._repository.delete(rental_id)
        return rental

    def get_repo(self):
        return self._repository
