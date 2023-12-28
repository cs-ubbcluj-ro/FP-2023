import unittest

from domain.flight import Flight
from domain.mytime import MyTime, MyDateTimeTime
from repository.flight_repo import FlightRepo
from repository.repo_exceptions import RepoExceptions
from service.flight_service import FlightController, FlightValidator
from service.flight_validator import ValidationException
from utils.file_utils import clear_file_content


class Test_repo(unittest.TestCase):
    def setUp(self):
        clear_file_content('test.txt')
        self.repository = FlightRepo('test.txt')

    def test_add(self):
        # This is added
        self.repository.add_flight(
            Flight('WIZZ123',
                   'Berlin',
                   MyTime(9, 5),
                   'Cluj',
                   MyTime(10, 0))
        )
        self.assertEqual(len(self.repository.list_flights()), 1)

        # flight_to_add with same id
        f = Flight('WIZZ123',
                   'Cluj',
                   MyTime(9, 26),
                   'Berlin',
                   MyTime(10, 2))
        self.assertRaises(RepoExceptions, self.repository.add_flight, f)
        self.assertEqual(len(self.repository.list_flights()), 1)

        # flight_to_add that arrives at the moment the first one departs
        f3 = Flight('WIZZ125',
                    'Cluj',
                    MyTime(9, 26),
                    'Berlin',
                    MyTime(9, 5))

        self.assertRaises(RepoExceptions, self.repository.add_flight, f3)
        self.assertEqual(len(self.repository.list_flights()), 1)

        # flight_to_add that departs at the moment the first one arrives
        f4 = Flight('WIZZ126',
                    'Cluj',
                    MyTime(10, 0),
                    'Milano',
                    MyTime(11, 15))

        self.assertRaises(RepoExceptions, self.repository.add_flight, f4)
        self.assertEqual(len(self.repository.list_flights()), 1)

    def tearDown(self):
        clear_file_content('test.txt')


class TestService(unittest.TestCase):
    def setUp(self):
        clear_file_content('test.txt')
        flight_repository = FlightRepo('test.txt')
        flight_validator = FlightValidator()
        self.__srv = FlightController(flight_repository, flight_validator)

    def test_add(self):
        self.__srv.add_flight('WIZZ1293',
                              'Barcelona',
                              MyTime(10, 0),
                              'Milano',
                              MyTime(11, 2))
        self.assertEqual(len(self.__srv.list_flights()), 1)

        # flight_to_add with too lengthy flight
        self.assertRaises(ValidationException, self.__srv.add_flight, 'WIZZ1292',
                          'Barcelona',
                          MyTime(10, 0),
                          'Milano',
                          MyTime(11, 45))
        self.assertEqual(len(self.__srv.list_flights()), 1)

    def tearDown(self):
        clear_file_content('test.txt')
class TimeTest(unittest.TestCase):

    def test_create_times_mytime(self):
        obj_time = MyTime(13, 24, 56)
        self.assertEqual(obj_time.hour, 13)
        self.assertEqual(obj_time.minute, 24)
        self.assertEqual(obj_time.second, 56)

        obj_time = MyTime(5, 4, 30)
        self.assertEqual(obj_time.hour, 5)
        self.assertEqual(obj_time.minute, 4)
        self.assertEqual(obj_time.second, 30)

        obj_time = MyTime(22, 41)
        self.assertEqual(obj_time.hour, 22)
        self.assertEqual(obj_time.minute, 41)
        self.assertEqual(obj_time.second, 0)

    def test_create_datetime_time(self):
        obj_time = MyDateTimeTime(13, 24, 56)
        self.assertEqual(obj_time.hour, 13)
        self.assertEqual(obj_time.minute, 24)
        self.assertEqual(obj_time.second, 56)

        obj_time = MyDateTimeTime(5, 4, 30)
        self.assertEqual(obj_time.hour, 5)
        self.assertEqual(obj_time.minute, 4)
        self.assertEqual(obj_time.second, 30)

        obj_time = MyDateTimeTime(22, 41)
        self.assertEqual(obj_time.hour, 22)
        self.assertEqual(obj_time.minute, 41)
        self.assertEqual(obj_time.second, 0)

    def test_subtract_times(self):
        t1 = MyTime(10, 20)
        t2 = MyTime(11, 30)
        diff_time = t2 - t1
        self.assertEqual(diff_time.hour, 1)
        self.assertEqual(diff_time.minute, 10)

        t1 = MyTime(9, 20)
        t2 = MyTime(10, 5)
        diff_time = t2 - t1
        self.assertEqual(diff_time.hour, 0)
        self.assertEqual(diff_time.minute, 45)

        t1 = MyTime(20, 15, 20)
        t2 = MyTime(22, 5, 25)
        diff_time = t2 - t1
        self.assertEqual(diff_time.hour, 1)
        self.assertEqual(diff_time.minute, 50)
        self.assertEqual(diff_time.second, 5)

        t1 = MyTime(20, 15, 20)
        t2 = MyTime(20, 16, 5)
        diff_time = t2 - t1
        self.assertEqual(diff_time.hour, 0)
        self.assertEqual(diff_time.minute, 0)
        self.assertEqual(diff_time.second, 45)

        t1 = MyTime(20, 15, 20)
        t2 = MyTime(21, 10, 19)
        diff_time = t2 - t1
        self.assertEqual(diff_time.hour, 0)
        self.assertEqual(diff_time.minute, 54)
        self.assertEqual(diff_time.second, 59)

    def test_add_time(self):
        t1 = MyTime(20, 15, 20)
        t2 = MyTime(1, 10, 0)
        print(t1 + t2)
