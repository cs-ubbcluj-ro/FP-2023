from src2023.lecture.livecoding.lecture10.repo.memory_repo import MemoryRepository
from src2023.lecture.livecoding.lecture10.services.car_services import CarService
from src2023.lecture.livecoding.lecture10.services.client_service import ClientService
from src2023.lecture.livecoding.lecture10.services.rental_services import RentalService
from src2023.lecture.livecoding.lecture11.ui.console import UI

# 0. Read the settings.properties file and set the repository types accordingly

# 1. Repositories
car_repo = MemoryRepository()
client_repo = MemoryRepository()
rental_repo = MemoryRepository()

# 2. Services
"""
ClientService depends on a MemoryRepository object that acts as a client repository
This dependency must be implemented as a constructor parameter => dependency injection
"""
client_service = ClientService(client_repo)
car_service = CarService(car_repo)
rental_service= RentalService(rental_repo,car_repo,client_repo)

# 3. UI
ui = UI(car_service,client_service,rental_service)
ui.start()
