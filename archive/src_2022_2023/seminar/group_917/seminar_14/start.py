from archive.src_2022_2023.seminar.group_917.seminar_14.repo.flight_repo import FlightRepository
from archive.src_2022_2023.seminar.group_917.seminar_14.services.flight_service import FlightServices
from archive.src_2022_2023.seminar.group_917.seminar_14.ui.ui import UI

flights_repo = FlightRepository("flights.txt")
flights_service = FlightServices(flights_repo)
flights_ui = UI(flights_service)
flights_ui.start()
