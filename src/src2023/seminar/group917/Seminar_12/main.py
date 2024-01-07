from ui.menu import Console
from service.flight_service import FlightController, FlightValidator
from repository.flight_repo import FlightRepo

if __name__ == "__main__":
    flight_repo = FlightRepo()
    flight_validator = FlightValidator()
    flight_controller = FlightController(flight_repo, flight_validator)
    console = Console(flight_controller)
    console.run()