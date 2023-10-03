class ValidatorException(Exception):
    def __init__(self, messageList):
        self._messageList = messageList

    def getMessage(self):
        return self._messageList

    def __str__(self):
        result = ""
        for message in self.getMessage():
            result += message
            result += "\n"
        return result
