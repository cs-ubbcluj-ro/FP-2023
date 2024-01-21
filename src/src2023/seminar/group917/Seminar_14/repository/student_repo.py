class RepositoryException(Exception):
    pass


class StudentAlreadyExistsException(RepositoryException):
    pass

class StudentNotFoundException(RepositoryException):
    pass

class StudentRepo:
    def __init__(self):
        self.__student_dict = {}

    def add_student(self, student):
        if student.id in self.__student_dict:
            raise StudentAlreadyExistsException()
        self.__student_dict[student.id] = student

    def delete_student(self, student):
        if student.id not in self.__student_dict:
            raise StudentNotFoundException()
        del self.__student_dict[student.id]

    def get_all(self):
        return self.__student_dict.values()
