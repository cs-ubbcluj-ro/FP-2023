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
import random
from datetime import date, timedelta

from archive.src_2022_2023.seminar.group_911.seminar_11.domain.car_validators import CarValidatorRO
from archive.src_2022_2023.seminar.group_911.seminar_11.domain.client import Client
from archive.src_2022_2023.seminar.group_911.seminar_11.domain.rental import Rental
from archive.src_2022_2023.seminar.group_911.seminar_11.domain.rental_validators import RentalValidator
from archive.src_2022_2023.seminar.group_911.seminar_11.repository.car_repo import car_repo_text_file

from archive.src_2022_2023.seminar.group_911.seminar_11.repository.client_repo import ClientRepo
from archive.src_2022_2023.seminar.group_911.seminar_11.repository.rental_repo import RentalRepository

# Initialize repositories
from archive.src_2022_2023.seminar.group_911.seminar_11.services.car_service import CarService
from archive.src_2022_2023.seminar.group_911.seminar_11.services.rental_service import RentalService

car_repo = car_repo_text_file()


# for c in car_repo.get_all():
#     print(c)


def generate_rentals(n: int):
    car_repo = car_repo_text_file()
    client = Client(100, "290010203445566", "Pop Maria")

    # TODO Generate n rentals
    # all rentals have the same client (Pop Maria)
    # rented car may vary
    # Rental - id, client, car, start_date, end_date
    # TODO - generate a random start date and end date
    # select a car from the list of existing cars
    # have a unique rental_id (start from 1000 and +1 for each instance)
    # return the list of rentals

    rental_id = 1000
    rentals = []
    while n > 0:
        rd = random.randint
        start_date = date(rd(2021, 2022), rd(1, 12), rd(1, 28))
        day_count = timedelta(days=rd(1, 10))
        end_here = start_date + day_count
        rentals.append(Rental(rental_id, start_date, end_here, client, random.choice(car_repo.get_all())))
        rental_id += 1
        n -= 1
    return rentals


# rentals = generate_rentals(10)
# print(rentals)

# NOTE you should be able to change the types of repos, services etc.
# car_repo = car_repo_bin_file()
client_repo = ClientRepo()

rent_repo = RentalRepository()
for rental in generate_rentals(100):
    rent_repo.add(rental)

# Start up services layer
# NOTE dependency injection of car repository for car service
car_service = CarService(car_repo, CarValidatorRO())

# client_service = ClientService(client_repo, ClientValidator())
rent_service = RentalService(rent_repo, car_service, RentalValidator())

# TODO Move this code to the UI
for r in rent_service.cars_sorted_by_rental_days():
    print(r)
"""
ui = UI(car_service, client_service, rent_service)
ui.start()
"""
