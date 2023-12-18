from datetime import time


class mytime(time):
    def __sub__(self, other):
        # NOTE Ignores microseconds :(
        if not isinstance(other, time):
            raise TypeError("Cannot subtract time from " + type(other))
        return abs((self.hour - other.hour) * 60 + self.minute - other.minute)
