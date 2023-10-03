class CarRentalException(Exception):
    def __init__(self, msg):
        self._message = msg
        
    def getMessage(self):
        return self._message
    
    def __str__(self):
        return self._message