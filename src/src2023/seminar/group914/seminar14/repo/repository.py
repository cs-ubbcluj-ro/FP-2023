from src2023.seminar.group914.seminar14.domain.student import Student


class Repo:
    def __init__(self):
        self.__data = {}
        self._load_from_file()

    def _load_from_file(self):
        try:
            with open("students.txt", 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            return

        for line in lines:
            line = line.strip()
            if line == "":
                continue
            tokens = line.split(',')
            id = int(tokens[0])
            name = tokens[1]
            group = tokens[2]
            st = Student(id, name, group)
            self.__data[id] = st

    def _save_to_file(self):
        with open("students.txt", 'w') as f:
            for el in self.__data.values():
                f.write(f"{el.id},{el.name},{el.group}\n")

    def add_student(self, student):
        if student.id in self.__data.keys():
            raise Exception("duplicate id")
        else:
            self.__data[student.id] = student
        self._save_to_file()

    def find_by_id(self, id):
        if id not in self.__data.keys():
            raise Exception("id not in the list")
        else:
            return self.__data[id]

    def delete_student(self, student):
        if student.id not in self.__data.keys():
            raise Exception("can not remove student")
        else:
            del self.__data[student.id]
        self._save_to_file()
