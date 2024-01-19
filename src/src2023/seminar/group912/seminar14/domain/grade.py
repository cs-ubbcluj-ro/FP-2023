from src2023.seminar.group912.seminar14.domain.laboratory import Laboratory
from src2023.seminar.group912.seminar14.domain.student import Student
from src2023.seminar.group912.seminar14.domain.idobject import IdObject


class Grade(IdObject):
    def __init__(self, _id: int, laboratory: Laboratory, student: Student, problem_number: int, value=None):
        super().__init__(_id)
        self.__laboratory = laboratory
        self.__student = student
        if 1 > problem_number > 20:
            raise ValueError("Invalid problem number")
        if value is not None and (1 > value > 10):
            raise ValueError("Invalid grade value")
        self.__problem_number = problem_number
        self.__value = value

    def __str__(self):
        return str(self.id) + ", lab: " + str(self.__laboratory) + " | student: " + str(
            self.__student) + " | problem: " + str(
            self.__problem_number) + " | grade: " + str(self.__value)
