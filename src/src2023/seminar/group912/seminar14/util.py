import random

from src2023.seminar.group912.seminar14.IdGenerator import IdGenerator
from src2023.seminar.group912.seminar14.domain.grade import Grade
from src2023.seminar.group912.seminar14.domain.laboratory import Laboratory
from src2023.seminar.group912.seminar14.domain.student import Student


def generateRandomStudents(n: int):
    id_gen = IdGenerator("student_id.txt")

    student_names = ["Mircea", "Ioan", "Mihai", "Sebastian", "Iustinian", "Miruna", "Samanta", "Claudia"]
    student_surnames = ["Bota", "Toda Pop", "Voica", "Biris", "Popa"]
    students = []
    for i in range(n):
        students.append(
            Student(id_gen.get_next_id(), random.choice(student_surnames) + " " + random.choice(student_names)))
    return students


def generateRandomLaboratories(n: int):
    id_gen = IdGenerator("labs_id.txt")
    lab_names = ["Maths", "English", "FP", "ASC", "Logic", "Algebruh", "Calculus", "Sport", "Biology", "Romanian",
                 "Spanish", "History", "Geography", "Arts", "Geometry", "OOP", "Computer Science", "TIC",
                 "Grammar", "Music"]
    lab_difficulty = ["for dummies", "advanced", "preparatory course", "high level", "low level", "retake"]
    labs = []
    for i in range(n):
        labs.append(
            Laboratory(id_gen.get_next_id(), random.choice(lab_names) + " " + random.choice(lab_difficulty)))
    return labs


def generateRandomGrades(n: int, students: list, laboratories: list):
    id_gen = IdGenerator("grades_id.txt")
    grades = []
    for i in range(n):
        grades.append(
            Grade(id_gen.get_next_id(), random.choice(laboratories), random.choice(students), random.randint(1, 20)))
    return grades
