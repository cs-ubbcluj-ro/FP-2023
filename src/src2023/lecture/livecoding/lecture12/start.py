from src2023.lecture.livecoding.lecture12.domain.exceptions import FlightAppException
from src2023.lecture.livecoding.lecture12.repo.FligthRepo import FlightRepo
from src2023.lecture.livecoding.lecture12.repo.memory_repo import MemoryRepository
from src2023.lecture.livecoding.lecture12.services.flight_service import FlightService
from src2023.lecture.livecoding.lecture12.services.flight_validator import FlightValidator
from src2023.lecture.livecoding.lecture12.services.settings import Settings
from src2023.lecture.livecoding.lecture12.ui.console import UI

# TODO Implement a binary file repo :)
settings = Settings.get_instance()

repo = None
try:
    repo = FlightRepo(settings.repo_file)
except FlightAppException:
    repo = MemoryRepository()

validator = FlightValidator()
# NOTE It's important that we pass the dependencies of the service here
# We can change the validator/repository we use without touching the Service class
# Ex. Next year you know how to write an SQLFlightRepo, you can make the existing
# service work with a database without changing its source code
service = FlightService(validator, repo)
ui = UI(service)
ui.start()
