from datetime import date

from archive.src_2022_2023.seminar.group_915.seminar_12.domain.validator_exception import ValidatorException


class Rental:
    def __init__(self, _id, start, end, client, car):
        self._id = _id
        self._client = client
        self._car = car
        self._start = start
        self._end = end

    @property
    def id(self):
        return self._id

    @property
    def client(self):
        return self._client

    @property
    def car(self):
        return self._car

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def __len__(self):
        return (self._end - self._start).days + 1

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Rental: " + str(self.id) + "\nCar: " + str(self.car) + "\nClient: " + str(
            self.client) + "\nPeriod: " + self.start.strftime("%Y-%m-%d") + " to " + self.end.strftime("%Y-%m-%d")


class RentalValidator:

    def validate(self, rental):
        if isinstance(rental, Rental) is False:
            raise TypeError("Not a Rental")
        _errorList = []
        now = date(2000, 1, 1)
        if rental.start < now:
            _errorList.append("Rental starts in past;")
        if len(rental) < 1:
            _errorList.append("Rental must be at least 1 day;")
        if len(_errorList) > 0:
            raise ValidatorException(_errorList)
