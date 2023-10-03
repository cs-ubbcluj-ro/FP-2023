class RepositoryException(Exception):
    def __init__(self, message):
        self._message = message

    def get_message(self):
        return self._message

    def __str__(self):
        return self._message