from src2023.seminar.group912.seminar12.domain.flight import Flight


class ValidationError(Exception):
    def __init__(self, messages: list):
        self.__messages = messages


class FlightValidator:
    def validate(self, flight: Flight):
        """
        Validate that flight object has valid fields and flight duration
        :param flight:
        :return: None, or ValidationError in case flight not valid
        """
        errors = []
        if flight.dep_city == flight.arr_city:
            errors.append("Flight should arrive at different airport")
        if flight.dep_time > flight.arr_time:
            errors.append("Flight departure time after arrival time")
        elif not 15 <= flight.arr_time - flight.dep_time <= 90:
            errors.append("Flights must be between 15 and 90 minutes!")
        if len(errors) > 0:
            raise ValidationError(errors)
