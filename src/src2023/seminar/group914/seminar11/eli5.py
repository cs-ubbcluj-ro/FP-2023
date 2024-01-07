"""
About undo/redo
    - Global operation (user can undo/redo operations that changed data in the app)
    - Undo can be applied as many times as there are operations in the program
    - Redo must be the next operation after an undo
    - Undo/redo is not persisted to file/db/etc.

There are 2 ways to implement it:
    1. Keep a copy of the program data at each operation
    Memento design pattern - https://refactoring.guru/design-patterns/memento
    + state-diffing (difference between program states)

    2. Keep a list /stack of the program's actions and reverse them at undo
    Command design pattern - https://refactoring.guru/design-patterns/command
"""


def my_function(a, b):
    return a + b


# we want to call my_function(5, 4) sometime in the future
# in Python, functions are first order objects (they behave like variables)

# do this at each program operation
fun = my_function
params = 5, 4

# do this when user hits undo
print(fun(*params))  # * is tuple unpacking
