# Uriesu Iulius
from archive.src_2022_2023.seminar.group_917.seminar_14.services.flight_service import FlightServices


class UI:

    def __init__(self, flight_services: FlightServices):
        self._flight_services = flight_services
        print('\nWelcome! In order to choose an option, type its corresponding number.')

    def start(self):
        options = {'1': self._display_all_flights,
                   '0': self._exit}

        while True:
            print('\nMenu:')
            print('\t1. Display all flights')
            print('\t0. Exit')

            opt = input('>>> ')
            opt = opt.strip()

            try:
                options[opt]()
            except KeyError:
                print('Invalid option')

    def _display_all_flights(self):
        for flight in self._flight_services.get_all():
            print(flight)

    @staticmethod
    def _exit():
        print('Exiting the application...')
        exit(0)
