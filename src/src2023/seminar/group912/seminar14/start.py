from src2023.seminar.group912.seminar14.repo.repository import Repository
from util import generateRandomGrades, generateRandomLaboratories, generateRandomStudents

students = generateRandomStudents(10)
studentRepo = Repository()
for s in students:
    studentRepo.store(s)

laboratories = generateRandomLaboratories(5)
labsRepo = Repository()
for l in laboratories:
    labsRepo.store(l)

grades = generateRandomGrades(20, students, laboratories)
gradesRepo = Repository()
for g in grades:
    gradesRepo.store(g)

print("students:")
print(studentRepo)

print("labs:")
print(labsRepo)

print("grades:")
print(gradesRepo)
