from datetime import date

from seminar.group_911.seminar_11.domain.exceptions import ValidatorException
from seminar.group_911.seminar_11.domain.rental import Rental


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
