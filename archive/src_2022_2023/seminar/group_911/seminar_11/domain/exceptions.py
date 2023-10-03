class ValidatorException(Exception):
    def __init__(self, message_list="Validation error!"):
        self._message_list = message_list

    @property
    def messages(self):
        return self._message_list

    def __str__(self):
        result = ""
        for message in self.messages:
            result += message
            result += "\n"
        return result


class CarException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


class CarValidationException(CarException):
    def __init__(self, error_list):
        self._errors = error_list

    def __str__(self):
        result = ''

        for er in self._errors:
            result += er
            result += '\n'
        return result
