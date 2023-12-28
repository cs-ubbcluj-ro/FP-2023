class ValidationException(Exception):
    def __init__(self, messages):
        self.messages = messages

    def __str__(self):
        return '\n'.join(self.messages)


class FlightValidator:
    def validate(self, flight):
        errors = []
        flight_duration = flight.get_duration()
        # Also check that flight_to_add doesn't leave and arrive at same airport, for instance
        if flight_duration.hour > 1 or (flight_duration.hour == 1 and flight_duration.minute > 30):
            errors.append("Duration cannot be greater than 1h30. ")
        if flight_duration.hour == 0 and flight_duration.minute < 15:
            errors.append("Duration cannot be smaller than 15 minutes. ")
        if len(errors) > 0:
            raise ValidationException(errors)