"""
What entities belong to the problem domain?

    Student
        - id, name, group

    Grade
        - student, laboratory, problem number, grade value

    Student groups ca be represented as strings


Implement an id generator
    https://codeshare.io/914

    - class which has a method called generate_id()
    - last generated id is saved to a text file
    - load the file in __init__
    - save the file after each id was generated
    - always returns a new id number


Things to do next
    1. StudentRepository
        - add, remove, find

    2. StudentService
        - add, remove
    3. UI (partially)
        - we skip for now

    4. function to generate some student objects
        - function generate_students(n : int)


"""