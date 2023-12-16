class ValidationException(Exception):
    def __init__(self, error_msg_list):
        self._error_messages = error_msg_list

    @property
    def error_messages(self):
        return self._error_messages

    def __str__(self):
        return "Validation error:" + "\n".join(self.error_messages)


class TaskValidationException(ValidationException):
    def __init__(self, error_msgs):
        ValidationException.__init__(self, error_msgs)

class PersonValidationException(ValidationException):
    def __init__(self, error_msgs):
        ValidationException.__init__(self, error_msgs)


class AssignmentValidationException(ValidationException):
    def __init__(self, error_msgs):
        ValidationException.__init__(self, error_msgs)
