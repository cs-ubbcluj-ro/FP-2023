import math
import unittest
from datetime import time, datetime, timedelta


class TimeHandlingException(Exception):
    pass


"""
Inherit from datetime class time, which has the following properties
    *hour, minute, second, (microsecond, tzinfo, fold)

Use:
 def __new__(cls, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
        Constructor.

        Arguments:

        hour, minute (required)
        second, microsecond (default to zero)
        tzinfo (default to None)
        fold (keyword only, default to zero)
    
"""


class MyTime(time):
    def __sub__(self, other):
        if not isinstance(other, MyTime):
            raise TimeHandlingException("Cannot subtract between MyTime and something else.")

        # assume t1>t2 if we do t1-t2
        diff_hours = self.hour - other.hour
        diff_mins = self.minute - other.minute
        diff_seconds = self.second - other.second

        if self.second < other.second:
            diff_seconds += 60
            diff_mins -= 1

        if self.minute < other.minute:
            diff_mins += 60
            diff_hours -= 1

        return MyTime(diff_hours, diff_mins,diff_seconds)

    def __add__(self, other):
        added_minutes = other.minute + self.minute
        no_hours, remainder_minutes = divmod(added_minutes, 60)
        print(no_hours, remainder_minutes)
        added_hours = self.hour + other.hour + no_hours

        return MyTime(added_hours, remainder_minutes)

    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ':' + str(self.second)


class MyDateTimeTime():
    def __init__(self, hours, minutes, seconds=0):
        # This actually creates a time with an associated (default) date - 1900-01-01
        self.__time = datetime.strptime(str(hours) + ':' + str(minutes) + ':' + str(seconds), "%H:%M:%S")

        # print(self.__time)

    def __sub__(self, other):
        if not isinstance(other, MyDateTimeTime):
            raise TimeHandlingException("Cannot subtract from MyDateTimeTime and " + str(type(other)))
        # Upside as opposed to MyTime: difference is done automatically, we just need to convert the total from seconds
        time_difference = self.__time - other.__time
        time_difference_secs = time_difference.total_seconds()
        difference_minutes = time_difference_secs // 60
        difference_seconds = time_difference_secs - (difference_minutes * 60)
        difference_hours = difference_minutes // 60
        difference_minutes = difference_minutes - (difference_hours * 60)
        return MyDateTimeTime(int(difference_hours), int(difference_minutes), int(difference_seconds))

    def __add__(self, other):
        # Addition also done 'automatically' given that we provide the expected format
        current_time = self.__time
        added_time = current_time + timedelta(0, seconds=other.__time.hour * 3600 + other.__time.minute * 60)
        return MyDateTimeTime(added_time.hour, added_time.minute, added_time.second)

    @property
    def hour(self):
        return self.__time.hour

    @property
    def minute(self):
        return self.__time.minute

    @property
    def second(self):
        return self.__time.second

    def __eq__(self, other):
        if not isinstance(other, MyDateTimeTime):
            raise TypeError("Cannot compare MyDateTimeTime and " + str(type(other)))
        return self.hour == other.hour and self.minute == other.minute

    # Downside to not using inheritance from a class that implements these
    # we have to explicitly implement them -> try running sorting objects of these type
    # on time fields without them
    def __le__(self, other):
        return self.__time <= other.__time

    def __lt__(self, other):
        return self.__time < other.__time

    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ':' + str(self.second)


