import random

from src2023.seminar.group914.seminar14.domain.student import Student
from src2023.seminar.group914.seminar14.repo.repository import Repo
from src2023.seminar.group914.seminar14.services.idgenerator import IdGenerator


def generate_students(n: int):
    name = ["Andrei", "Eduard", "Mihai", "Mariana", "Veronica",
            "Andreea", "Victor", "Ariana", "Aris", "Cristian",
            "Cosmin", "Mara", "Patricia", "Bogdan"]
    groups = ["100", "200", "300", "400", "500"]

    id_generator = IdGenerator()
    students = []
    while n > 0:
        stud_name = random.choice(name)
        group = int(random.choice(groups)) + random.randint(0, 5)
        students.append(Student(id_generator.generate_id(), stud_name, str(group)))
        n -= 1
    return students


repo = Repo()
for s in generate_students(10):
    repo.add_student(s)
