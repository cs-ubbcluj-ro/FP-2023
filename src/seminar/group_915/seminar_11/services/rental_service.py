from seminar.group_915.seminar_11.domain.rental import Rental


# DTO - data transfer object => moving things between layers
class CarRentalDaysDTO:
    def __init__(self, car, rental_days):
        self._car = car
        self._rental_days = rental_days

    @property
    def car(self):
        return self._car

    @property
    def rental_days(self):
        return self._rental_days

    def __str__(self):
        return str(self.rental_days) + " for car " + str(self.car)


class RentalService:
    def __init__(self, repo, rental_validator, car_service):
        self._repo = repo
        self._validator = rental_validator
        self._car_service = car_service

    # 1. create rental instance in UI
    # 2. create rental instance in service (x)
    def add(self, rental_id, start, end, client, car):
        # 1. create Rental instance
        rent = Rental(rental_id, start, end, client, car)
        # 2. validate it
        self._validator.validate(rent)
        # 3. add to repo
        self._repo.add(rent)

    """
     The list of all cars in the car pool sorted by number of days 
    they were rented.
    """

    def statistic_cars_by_rental_days(self):
        rental_days = {}

        for rental in self._repo.get_all():
            if rental.car.car_id in rental_days:
                rental_days[rental.car.car_id] += len(rental)
            else:
                rental_days[rental.car.car_id] = len(rental)

        # all cars that were never rented
        for car in self._car_service.get_all():
            if car.car_id not in rental_days:
                rental_days[car.car_id] = 0
        """
        n cars, m rentals
        before: O(n*m) + O(n) => O(n*m)
        after: O(m) + O(n) => O(max(n,m))
        """

        result = []
        for kv in rental_days:
            car = self._car_service.get(kv)
            result.append(CarRentalDaysDTO(car, rental_days[kv]))

        # 1. first sort by license plate numbers
        result.sort(key=lambda x: x.car.car_id)

        # 2. sort by number of rental days (TimSort -> stable)
        result.sort(key=lambda x: x.rental_days, reverse=True)
        return result
