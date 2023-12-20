from src2023.seminar.group912.seminar12.repo.FligthRepo import FlightRepo
from src2023.seminar.group912.seminar12.services.flight_service import FlightService
from src2023.seminar.group912.seminar12.services.flight_validator import FlightValidator
from src2023.seminar.group912.seminar12.ui.console import UI

repo = FlightRepo()
validator = FlightValidator()
# NOTE It's important that we pass the dependencies of the service here
# We can change the validator/repository we use without touching the Service class
# Ex. Next year you know how to write an SQLFlightRepo, you can make the existing
# service work with a database without changing its source code
service = FlightService(validator, repo)
ui = UI(service)
ui.start()
