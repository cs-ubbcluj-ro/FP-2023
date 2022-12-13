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
         The list of all cars in the car pool sorted by number of days they were rented.
         The list of clients sorted descending by the number of cars they have rented.

    The application must have support for unlimited undo/redo with cascading.
"""
import datetime
import random

from seminar.group_917.seminar_11.domain.car import car
from seminar.group_917.seminar_11.domain.car_validators import CarValidatorRO
from seminar.group_917.seminar_11.domain.client import Client
from seminar.group_917.seminar_11.domain.client_validators import ClientValidator
from seminar.group_917.seminar_11.domain.rental import Rental
from seminar.group_917.seminar_11.domain.rental_validators import RentalValidator
from seminar.group_917.seminar_11.repository.car_repo import car_repo_text_file
from seminar.group_917.seminar_11.repository.client_repo import ClientRepo
from seminar.group_917.seminar_11.repository.rental_repo import RentalRepository
from seminar.group_917.seminar_11.services.car_service import CarService
from seminar.group_917.seminar_11.services.client_service import ClientService
from seminar.group_917.seminar_11.services.rental_service import RentalService
from seminar.group_917.seminar_11.ui.ui import UI


def generate_rentals(n: int):
    car_repo = car_repo_text_file()
    client = Client(100, "2900101223344", "Pop Ioana")

    rnd = random.randint

    rentals = []
    rental_id = 1000
    while n > 0:
        rented_car = random.choice(car_repo.get_all())
        start_date = datetime.date(rnd(2021, 2022), rnd(1, 12), rnd(1, 28))
        rental_len = rnd(1, 20)
        # NOTE date + timedelta = date
        end_date = start_date + datetime.timedelta(days=rental_len)
        r = Rental(rental_id, start_date, end_date, client, rented_car)
        rental_id += 1
        rentals.append(r)
        n -= 1
    return rentals


"""
How to assemble all program layers :)
"""
# 1. Start bottom-up with the repo
car_repo = car_repo_text_file()
client_repo = ClientRepo()
rental_repo = RentalRepository()
# print(generate_rentals(20))
for r in generate_rentals(20):
    rental_repo.add(r)

# 2. Services
car_service = CarService(car_repo, CarValidatorRO())
rent_service = RentalService(rental_repo, RentalValidator())

# TODO Call from the UI
for c in rent_service.cars_by_number_of_rental_days():
    print(c)

# client_service = ClientService(client_repo, ClientValidator())

# 3. UI
# ui = UI(car_service, client_service, rent_service)
# ui.start()

"""
    Statistics
         The list of all cars in the car pool sorted by number of days 
        they were rented.
"""

# for car in generate_cars(20):
#     car_repo.add(car)
