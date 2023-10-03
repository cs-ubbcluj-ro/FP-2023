from archive.src_2022_2023.seminar.group_917.seminar_14.domain.flight import Flight


class FlightRepository:
    def __init__(self, fileName):
        self._fileName = fileName
        self._data = []
        file = open(self._fileName, 'r')
        for line in file.readlines():
            id, departureCity, departureTime, arrivalCity, arrivalTime = line.split(",")
            self._data.append(Flight(id, departureCity, departureTime, arrivalCity, arrivalTime.strip()))
        file.close()

    def get_all(self):
        return self._data

    def __len__(self):
        return len(self._data)


# TODO Move to services layer :)
def radar_failure():
    repo = FlightRepository("../flights.txt")
    flights = repo.get_all()

    flights.sort(key=lambda key: key.arrival_time)

    for f in flights:
        print(f)

    result = [flights.pop(0)]
    for flight in flights:
        if flight.departure_time > result[-1].arrival_time:
            result.append(flight)

    print("-" * 50)
    for f in result:
        print(f)
