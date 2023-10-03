"""
Write an application that manages a group of students.
Each student has a unique id (string), a name (string) and a grade (integer).
The application will have a menu-driven user interface and will provide the
following features:

    1. Add a student
        - adds the student with the given id, name and grade to the list.
        - error if giving existing id, the name or grade fields not given or
        empty

    2. Delete a student
        - deletes the student with the given id from the list
        - error if non-existing id given

    3. Show all students
        - shows all students in descending order of their grade

    4. Show students whose grade is > than given one, ordered in descending
    order of grade

    5. exit
        - exit the program

    Observations:
        - Add 10 random students at program startup
        - Write specifications for non-UI functions
        - Each function does one thing only, and communicates via parameters and return value
        - The program reports errors to the user. It must also report errors from non-UI functions!
        - Make sure you understand the student's representation
        - Try to reuse functions across functionalities (Less code to write and test)
        - Don't use global variables!
"""
import random


#
# Write the implementation for Seminar 06 in this file
#

#
# Write below this comment
# Functions to deal with students -- list representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

# 9981, Popescu Ioana, 10 => ["9981", "Popescu Ioana", 10]
def create_student(id, name: str, grade: int):
    """
    Create a new student
    :return: The new student, or None if any of the fields are empty
    """
    return [id, name, grade]


def get_id(student):
    return student[0]


def get_name(student):
    return student[1]


def get_grade(student):
    return student[2]


def to_str(student):
    """
    Return the str representation of the student
    :param student: Given student
    :return: For student 9981, Popescu Ioana, 10, return
    "id: 9981; name: Popescu Ioana has grade 10"
    """
    return "id: " + str(student[0]) + "; name: " + str(student[1]) + " id: " + str(student[2])


#
# Write below this comment
# Functions to deal with students -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
# TODO Copy the exact function signatures from previous block and implement
# them as dict

# 9981, Popescu Ioana, 10 => {"id": "9981","name": "Popescu Ioana","grade": 10}

#
# Write below this comment
# Functions that deal with the required functionalities properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def generate_students(count: int):
    family_name = ['Popescu', 'Marian', 'Pop', 'Lazarescu', 'Dincu']
    given_name = ['Anca', 'Emilia', 'Liviu', 'Marius']

    students = []

    while count > 0:
        family = random.choice(family_name)
        given = random.choice(given_name)
        full_name = family + " " + given

        student = create_student(str(9000 + count), full_name, random.randint(4, 10))
        students.append(student)
        count -= 1
    return students


# generate_students(5)

def add_student(list_of_students: list, new_student):
    """
    Add the new student to the list
    :param list_of_students: The list of all students in the program
    :param new_student: The new guy
    :return: 0 on success, 1 if duplicate student id
    """
    for std in list_of_students:
        if get_id(std) == get_id(new_student):
            return 1
    list_of_students.append(new_student)
    return 0


def delete_student(student_list: list, deleted_id: str):
    for index in range(0, len(student_list)):
        if get_id(student_list[index]) == deleted_id:
            student_list.pop(index)
            return 0
    return 1


def sort_by_grade(student_list):
    n = len(student_list)
    ok = True
    while ok is True:
        ok = False
        for i in range(0, n - 1):
            if get_grade(student_list[i]) < get_grade(student_list[i + 1]):
                ok = True
                student_list[i], student_list[i + 1] = student_list[i + 1], student_list[i]


#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#
def print_students(students: list):
    print("\nAll students:")
    for s in students:
        print(to_str(s))


def show_good_grades(student_list: list, grade: int):
    good_grade_students = []
    for student in student_list:
        if get_grade(student) > grade:
            add_student(good_grade_students, student)

    good_grade_students.sort(key=lambda x: x[2], reverse=True)

    # sort_by_grade(good_grade_students)

    return good_grade_students


def start():
    # TODO What do we need here?
    # 1. Print main menu
    # 2. Read user choice -> call appropriate function
    # 3. Print out any error message
    # 4. Exit !?
    student_list = generate_students(10)
    # student_list = []

    print("Command options:\n", "1. Add student\n2. Delete student\n4. Print student filtered by grade\n0. Exit !?")
    while True:
        print_students(student_list)
        task = input("Input the command:")
        if task == "1":
            # TODO We need some more validation, move to a separate function
            id = input("Id:")
            name = input("Name:")
            grade = int(input("Grade:"))
            # add_student(student_list, create_student(id, name, grade))
            add_student(new_student=create_student(id, name, grade), list_of_students=student_list)

        elif task == "2":
            id = input("id:")
            if (delete_student(student_list, id) == 1):
                print("Student not found")
        elif task == "4":
            grade = int(input("grade:"))
            for student in show_good_grades(student_list, grade):
                print(to_str(student))
        elif task == "0":
            break
        else:
            print("Bad command or file name :)")


if __name__ == "__main__":
    start()
