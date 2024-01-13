class RepositoryExceptions(Exception):
    def __init__(self, error_message):
        self.__error_message = error_message

    @property
    def error_message(self):
        return self.__error_message

    def __str__(self):
        return "Repo error: " + str(self.error_message)


class OutsideOfBoundsError(RepositoryExceptions):
    def __init__(self):
        RepositoryExceptions.__init__(self, "Place outside of bounds")


class AlreadyHitPlaceError(RepositoryExceptions):
    def __init__(self):
        RepositoryExceptions.__init__(self, "Place already hit")
