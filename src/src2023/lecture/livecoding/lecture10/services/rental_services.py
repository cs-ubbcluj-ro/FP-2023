from src2023.lecture.livecoding.lecture10.domain.car import Car
from src2023.lecture.livecoding.lecture10.repo.memory_repo import MemoryRepository


class CarRentalDaysDTO:
    def __init__(self, car: Car, day_count: int):
        self.__car = car
        self.__days = day_count

    @property
    def car(self):
        return self.__car

    @property
    def day_count(self):
        return self.__days

    def __lt__(self, other):
        return self.day_count <= other.day_count

    def __str__(self):
        return "rented for " + str(self.day_count) + ", car is " + str(self.car)

    def __repr__(self):
        return str(self)


class RentalService:
    def __init__(self, rental_repo: MemoryRepository, car_repo: MemoryRepository, client_repo: MemoryRepository):
        # NB -- MemoryRepository can be replaced by any class derived from it
        # it could actually be a BinaryFileRepository(MemoryRepository),
        # or TextFileRepository(MemoryRepository)
        self.__rental_repo = rental_repo
        self.__car_repo = car_repo
        self.__client_repo = client_repo

    """
    statistic: the list of the most rented cars (cars that have the most
    number of rental days), sorted desc by the number of rental days
        rental_services.py
            a. get the list of all cars
            b. get the list of rentals for each car
            c. get the total rental days for each car
            d. sort them desc (use a DTO - data transfer object)
            e. return the list to the UI
    """

    def most_rented_cars(self) -> list:
        # 1. get all cars
        all_cars = []
        for c in self.__car_repo:  # enabled by __iter__, __next__
            all_cars.append(c)

        all_rentals = []
        for r in self.__rental_repo:
            all_rentals.append(r)

        # 2. get all rentals for each car
        car_rentals = {}  # keys are car id's, values are rental lists
        for rental in self.__rental_repo:
            rented_car_id = rental.car.id
            if rented_car_id not in car_rentals:
                car_rentals[rented_car_id] = [rental]
            else:
                car_rentals[rented_car_id].append(rental)

        # print("car rental lists")
        # for cr in car_rentals:
        #     print(cr, car_rentals[cr])

        #  3. get the total rental days for each car
        car_rental_days = {}
        for car_id in car_rentals:
            car_rental_days[car_id] = 0
            for rental in car_rentals[car_id]:
                car_rental_days[car_id] += len(rental)

        # 4. build the DTO list
        result = []
        for car_id in car_rental_days:
            item = CarRentalDaysDTO(self.__car_repo[car_id], car_rental_days[car_id])
            result.append(item)
        # 5. sort the DTO list
        result.sort(reverse=True)

        return result
