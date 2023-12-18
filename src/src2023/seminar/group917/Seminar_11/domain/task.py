# Extra-reading: dataclasses


class Task:

    def __init__(self, id, description, deadline_day, deadline_month, status):
        self._id = id
        self._description = description
        self._deadline_day = deadline_day
        self._deadline_month = deadline_month
        self._status = status

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def deadline_day(self):
        return self._deadline_day

    @property
    def deadline_month(self):
        return self._deadline_month

    @property
    def status(self):
        return self._status

    @description.setter
    def description(self, descr):
        self._description = descr

    @deadline_day.setter
    def deadline_day(self, deadline_day):
        self._deadline_day = deadline_day

    @deadline_month.setter
    def deadline_month(self, deadline_month):
        self._deadline_month = deadline_month

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def complete_date(self) -> str:
        return str(self._deadline_day) + '/' + str(self._deadline_month)

    def __eq__(self, other):
        if type(other) != Task:
            return False

        return self.id == other.id

    def __str__(self):
        return "ID: " + str(
            self.id) + " | " + "Description: " + self.description + " | " + "Deadline:" + str(
            self.complete_date) +' | Status: ' + self.status
