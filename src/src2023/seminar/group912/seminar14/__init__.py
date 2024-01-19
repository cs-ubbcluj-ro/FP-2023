"""
-= domain =-
    class Student
        - id, name, group

    class Laboratory
        - id, name

    class Grade
        - student, laboratory, laboratory problem number (1 -- 20), value (None, 1 --- 10)
        - value is None at lab assignment

    def generate_students(n : int) -> list[Student]
    def generate_laboratories(n : int) -> list[Laboratory]
    def generate_grades(n : int, list[Student], list[Laboratory]) -> list[Grade]


-= repository =-
    class Repository (works with text files directly)
        - add, delete, find
        - save_file, load_file

"""
