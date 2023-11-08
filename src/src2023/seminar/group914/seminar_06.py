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
from random import choice, randint

"""
    Student representation functions are below 
"""


# student as a dict
def create_student(_id: str, name: str, grade: int):
    # What to do in case of bad input params??!!
    # V1 - return error code
    # V2 - use exceptions
    if len(_id) == 0 or len(name) < 3 or grade < 1 or grade > 10:
        raise ValueError("Invalid data to create student")

    # encapsulation -- keep everything having to do with the student in one place
    # return {"id": _id, "name": name, "grade": grade}
    return [_id, name, grade]


def get_id(student) -> str:
    # return student["id"]
    return student[0]


def get_name(student) -> str:
    # return student["name"]
    return student[1]


def get_grade(student) -> int:
    # return student["grade"]
    return student[2]


def to_str(student) -> str:
    return "ID: " + get_id(student) + ", name: " + get_name(student) + ", grade: " + str(get_grade(student))


"""
    Program functionalities (non-UI) are here
"""


def find_by_id(student_list: list, _id: str):
    """
    Return the student with given id, None if it could not be found
    :param student_list: List of students
    :param _id: The id to search for
    :return: The student, or None if could not be found
    """
    for s in student_list:
        if get_id(s) == _id:
            return s
    # student was not found
    return None


def generate_random_students(n: int) -> list:
    """
    Generate n pseudo-random students
    :param n: number of students
    :return: The list of generated students
    """
    family_names = ["Pop", "Marian", "Boldar", "Poescu", "Vranceanu"]
    given_name = ["Anca", "Emilia", "John", "Timotei", "Vlad"]
    current_id = 100

    result = []

    while n > 0:
        name = choice(family_names) + " " + choice(given_name)
        student = create_student(str(current_id), name, randint(1, 10))
        result.append(student)
        current_id += 1
        n -= 1
    return result


def add_student(student_list: list, student):
    """
    Add the given student to the list
    :param student_list: List of students
    :param student: The new student
    :return: None
    Raises ValueError in case of duplicate student id
    """
    if find_by_id(student_list, get_id(student)) is not None:
        raise ValueError("Duplicate student id - " + get_id(student))

    # alternative for code above
    # for s in student_list:
    #     if get_id(s) == get_id(student):
    #         raise ValueError("Duplicate student id - " + get_id(student))

    # if we get here => no error was raised
    student_list.append(student)


def delete_student(student_list: list, _id: str):
    """
    Delete student with given id
    :param student_list: The list of students
    :param _id: Id of student to delete
    :return: None
    Raise ValueError if student with given id does not exist
    """
    student = find_by_id(student_list, _id)
    if student is None:
        raise ValueError("Student not found")
    student_list.remove(student)


"""
    UI is below
"""


def print_menu():
    print("1. Display all students")
    print("2. Add a student")
    print("3. Delete a student")
    print("0. Exit")


def add_student_ui(students: list):
    try:
        _id = input("student id: ")
        name = input("student name: ")
        # might raise ValueError in case an str is provided that cannot be
        # converted to an int
        grade = int(input("student grade: "))

        # try / except creates its own scope for variables
        student = create_student(_id, name, grade)
        # FIXME What if multiple students have same ID ?
        add_student(students, student)
    except ValueError as ve:
        print("There was an error!")
        print(str(ve))


def delete_student_ui(students: list):
    _id = input("Student id: ")
    try:
        delete_student(students, _id)
    except ValueError as ve:
        print(str(ve))


def display_students_ui(students: list):
    for s in students:
        print(to_str(s))


def start():
    # generate some input data so we don't have to click around too much
    students = generate_random_students(10)

    # references to functions we call for each option
    functions = {"1": display_students_ui, "2": add_student_ui, "3": delete_student_ui}

    while True:
        print_menu()
        option = input(">")

        if option in functions:
            functions[option](students)
        elif option == "0":
            print("bye!")
            return
        else:
            print("Invalid menu option!")

    # if option == "1":
    #     display_students_ui(students)
    # elif option == "2":
    #     add_student_ui(students)
    # elif option == "3":
    #     delete_student_ui(students)
    # elif option == "0":
    #     print("bye!")
    #     return
    # else:
    #     # not a valid option
    #     print("Invalid menu option!")


if __name__ == "__main__":
    start()
