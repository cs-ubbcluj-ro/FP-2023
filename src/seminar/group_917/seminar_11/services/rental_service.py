from seminar.group_917.seminar_11.domain.rental import Rental


class CarRentalDaysDTO():
    def __init__(self, car, rental_days):
        self._car = car
        self._days = rental_days

    @property
    def car(self):
        return self._car

    @property
    def rental_day(self):
        return self._days

    @rental_day.setter
    def rental_day(self, new_value):
        self._days = new_value

    def __repr__(self):
        return str(self.rental_day) + " days for car " + str(self.car)


class RentalService:
    def __init__(self, rental_repo, rental_validator):
        self._repo = rental_repo
        self._validator = rental_validator

    def add_rental(self, rental_id, start_date, end_date, rented_car, client):
        # 1. build rental instance
        r = Rental(rental_id, start_date, end_date, client, car=rented_car)
        # 2. validate it
        self._validator.validate(r)
        # 3. store it
        self._repo.add(r)

    """
        Statistics
             The list of all cars in the car pool sorted by number of days 
            they were rented.
    """

    def cars_by_number_of_rental_days(self):
        # TODO Add cars that have no recorded rentals
        # keys are license plates, values are DTO instances
        # DTO = data transfer object
        dtos = {}

        for rental in self._repo.get_all():
            if rental.car.car_id in dtos:
                # not the first rental of this car
                # add the len of current rental to previous value
                dtos[rental.car.car_id].rental_day += len(rental)
            else:
                # first time we see this car
                dtos[rental.car.car_id] = CarRentalDaysDTO(rental.car, len(rental))

        # lists can be sorted, dicts not so much :(
        result = list(dtos.values())

        # NOTE how to sort (1) define __le__ in DTO, (2) sort key
        result.sort(key=lambda x: x.rental_day, reverse=True)

        return result
