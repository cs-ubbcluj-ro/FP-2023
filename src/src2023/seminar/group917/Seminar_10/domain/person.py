import datetime


class Person:
    def __init__(self, cnp, name):
        self._cnp = cnp
        self._name = name
        self._date_of_birth = self._compute_date_of_birth()

    @property
    def cnp(self):
        return self._cnp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def birth_year(self):

        return self._date_of_birth.year

    @property
    def birth_month(self):
        return self._date_of_birth.month

    @property
    def birth_day(self):
        return self._date_of_birth.day

    def _compute_date_of_birth(self) -> datetime.date:
        """
        Computes date of birth of the person
        """
        year = int(self._cnp[1:3])
        month = int(self._cnp[3:5])
        day = int(self._cnp[5:7])
        if year > 10:
            year = 1900 + year
        else:
            year = 2000 + year
        date_of_birth = datetime.date(year, month, day)
        return date_of_birth

    def __eq__(self, other):
        if type(other) != Person:
            return False
        return self.cnp == other.cnp

    def __str__(self):
        return 'CNP: ' + self.cnp + ' | Name: ' + self.name + ' | Date of birth: ' + str(self.date_of_birth)
