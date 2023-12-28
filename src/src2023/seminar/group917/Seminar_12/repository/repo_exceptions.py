class RepoExceptions(Exception):
    pass


class FlightNotFoundException(RepoExceptions):
    def __init__(self, flight_id):
        super().__init__("Could not find the flight with id: "+str(flight_id))


class RepoFileNotFoundException(RepoExceptions):
    def __init__(self, filename):
        super().__init__("File: "+str(filename)+" was not found.")


