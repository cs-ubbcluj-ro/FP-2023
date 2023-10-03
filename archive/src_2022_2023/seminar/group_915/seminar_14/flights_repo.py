from datetime import datetime, time

from archive.src_2022_2023.seminar.group_915.seminar_14.flight import Flight


class TextFlightRepository:
    def __init__(self, file_name: str):
        self._file_name = file_name
        self._flights = []
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "r")
        for line in file:
            # remove ","
            line_split = line.split(",")
            # remove last \n
            line_split[-1] = line_split[-1][:-1]
            departure_time = datetime.strptime(line_split[2], "%H:%M").time()
            arrival_time = datetime.strptime(line_split[4], "%H:%M").time()
            flight = Flight(line_split[0], line_split[1], departure_time, line_split[3], arrival_time)
            self._flights.append(flight)

    def get_all(self):
        return self._flights


if __name__ == "__main__":
    repo = TextFlightRepository("flights.txt")
    for flight in repo.get_all():
        print(flight)

    t1 = time(hour=18, minute=10, tzinfo=None)
    t2 = time(hour=18, minute=11, second=45, tzinfo=None)
    # TODO Take a look at time subtraction
    # print(t2 - t1)
