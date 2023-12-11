"""
Here we would also start up the UI
"""
from src2023.lecture.livecoding.lecture10.repo.memory_repo import MemoryRepository
from src2023.lecture.livecoding.lecture10.services.rental_services import RentalService
from src2023.lecture.livecoding.lecture10.domain.rental import generate_rentals

car_repo = MemoryRepository()
client_repo = MemoryRepository()
rental_repo = MemoryRepository()

# generate some data
cars, clients, rentals = generate_rentals(100)
for c in cars:
    car_repo.add(c)

for c in clients:
    client_repo.add(c)

for r in rentals:
    rental_repo.add(r)

# print(len(car_repo), len(client_repo), len(rental_repo))

# TODO Careful about the order of the parameters
rental_serv = RentalService(rental_repo, car_repo, client_repo)

# TODO This should be called in the UI
result = rental_serv.most_rented_cars()
for r in result:
    print(r)
