class CarRentalException(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return str(self.__msg)
