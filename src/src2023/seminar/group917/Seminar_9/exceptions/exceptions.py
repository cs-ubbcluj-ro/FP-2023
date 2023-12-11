class RepositoryError(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "Repository Exception: " + str(self.__msg)

class DuplicateIDException(RepositoryError):
    def __init__(self):
        RepositoryError.__init__(self, "There is already an entity with that id. ")