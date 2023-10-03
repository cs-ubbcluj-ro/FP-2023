from archive.src_2022_2023.seminar.group_911.seminar_14.domain.flight import Flight
import time


class FlightsRepo:

    def __init__(self, filename: str):
        self._data = {}
        self._filename = filename
        self._load_file()

    def _load_file(self):
        lines = []
        try:
            fin = open(self._filename, "rt")
            lines = fin.readlines()
            fin.close()
        except IOError:
            pass
        for line in lines:
            current_line = line.strip().split(",")
            d_time = time.strptime(current_line[2], "%H:%M")
            a_time = time.strptime(current_line[4], "%H:%M")
            flight = Flight((current_line[0]), current_line[1], d_time,
                            current_line[3], a_time)
            self.add(flight)
            print(flight.id)

    def add(self, flight: Flight):
        if flight.id in self._data:
            raise ValueError("Flight already in repo")
        self._data[flight.id] = flight
        self._save_file()

    def _save_file(self):
        fout = open(self._filename, "wt")
        flights = list(self._data.values())
        for flight in flights:
            d_time = time.strftime("%H:%M", flight.departure_time)
            a_time = time.strftime("%H:%M", flight.arrival_time)
            flight_string = str(
                flight.id) + "," + flight.departure_city + "," + d_time + "," + flight.arrival_city + "," + a_time + "\n"
            fout.write(flight_string)
        fout.close()

    def get_all(self):
        return list(self._data.values())

    @property
    def file_name(self):
        return self._filename

    def __len__(self):
        return len(self._data)
