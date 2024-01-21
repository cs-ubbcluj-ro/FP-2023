from colorama import Fore, Style

from src2023.seminar.group917.Seminar_14.service.student_service import UndoRedoException


class Console:
    def __init__(self, service):
        self.__service = service

    def print_menu(self):
        print('1. Add student')
        print('2. Print all students')
        print('3. Undo')
        print('4. Redo')

        print('5. Exit')

    def run(self):
        while True:

            self.print_menu()
            option = input(">>")
            if option == '1':
                self.add_student()
            elif option == '2':
                self.print_students()
            elif option == '3':
                self.__service.undo()
            elif option == '4':
                self.__service.redo()
            else:
                break

    def add_student(self):
        name = input("Student name:")
        group = input("Student group")
        self.__service.add_student(name, group)

    def print_students(self):
        students = self.__service.get_all()
        for student in students:
            print(student)

