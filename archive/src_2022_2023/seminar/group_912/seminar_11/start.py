"""
Create an application for a car rental business using a console based user interface.
The application must allow keeping records of the company’s list of clients, existing car pool and rental history.
The application must allow its users to manage clients, cars and rentals in the following ways:
    Clients
         Add a new client. Each client is a physical person having a unique ID (driver license series), name, age.
         Update the data for any client.
         Remove a client from active clients. Note that removing a client must not remove existing car rental statistics.
         Search for clients based on ID and name [both at the same time]
         All client operations must undergo proper validation!
    Cars
         Add a new car to the car pool. Each car must have a valid license plate number, a make and model taken from a
        list of makes and models. In addition, each car will have a color.
         Remove a car from the car pool.
         Search for cars based on license number, make and model and color.
            [search with no parameters displays everything, omitting a param disregards it]
            [make = VW, model = Polo, CJ01ABC], [make = VW, model = Polo, CJ01XYZ]
         All car operations must undergo proper validation!
    Rentals
         An existing client can rent one or several cars from the car pool for a determined period. When rented, a car
        becomes unavailable for further renting.
         When a car is returned, it becomes available for renting once again.
         Search the rental history of a given client, car, or all rentals during any given period.
    Statistics
         The list of all cars in the car pool sorted by number of days
        they were rented.

         The list of clients sorted descending by the number of cars they
        have rented.

    The application must have support for unlimited undo/redo with cascading.
"""
from archive.src_2022_2023.seminar.group_912.seminar_11.domain.car_validators import CarValidatorRO
from archive.src_2022_2023.seminar.group_912.seminar_11.domain.client import Client
from archive.src_2022_2023.seminar.group_912.seminar_11.domain.rental_validators import RentalValidator
from archive.src_2022_2023.seminar.group_912.seminar_11.repository.car_repo import car_repo_text_file
from archive.src_2022_2023.seminar.group_912.seminar_11.repository.rental_repo import RentalRepository

# Assemble the layers bottom up
from archive.src_2022_2023.seminar.group_912.seminar_11.services.car_service import CarService
from archive.src_2022_2023.seminar.group_912.seminar_11.services.rental_service import RentalService

import random
from datetime import date, timedelta


def generate_rentals(n: int, rental_service):
    # NOTE generate n rentals here
    # this client rents all cars
    c1 = Client(1000, "290010203445566", "Popescu Ana")
    # car_repo holds the cars that will be rented out
    car_repo = car_repo_text_file()
    rental_id = 1000
    rnd = random.randint

    while n > 0:
        car = random.choice(car_repo.get_all())
        start = date(rnd(2021, 2022), rnd(1, 12), rnd(1, 28))
        end = start + timedelta(days=rnd(1, 20))
        rental_service.add(rental_id, start, end, c1, car)
        rental_id += 1
        n -= 1


car_repo = car_repo_text_file()
rental_repo = RentalRepository()

# NOTE You can switch the repo and validator you use without changing
# the service class source code
# NOTE this is named "dependency injection"
car_service = CarService(car_repo, CarValidatorRO())
rental_service = RentalService(rental_repo, car_service, RentalValidator())
generate_rentals(100, rental_service)

statistic_result = rental_service.statistic_cars_by_rental_days()
for sr in statistic_result:
    print(sr)

# for s in statistic_result:
#     print(s)

# ui = UI( < pass all services here >)
# ui.start()

# for car in generate_cars(20):
#     car_repo.add(car)
