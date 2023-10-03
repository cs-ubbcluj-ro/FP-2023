from archive.src_2022_2023.seminar.group_911.seminar_14.services.flights_service import FlightService
from archive.src_2022_2023.seminar.group_911.seminar_14.repo.repo import FlightsRepo
from archive.src_2022_2023.seminar.group_911.seminar_14.ui.ui import UI

repo = FlightsRepo("flights.txt")
services = FlightService(repo)
ui = UI(services)
ui.RUN_PROGRAM()
