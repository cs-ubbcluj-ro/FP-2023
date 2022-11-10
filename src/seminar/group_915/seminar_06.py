"""
Write an application that manages a list of rectangles.
Each rectangle is represented using its two opposite corners (x1, y1) and (x2, y2)
The application will have a menu-driven user interface and will provide the following features:

    1. Add a rectangle
        - adds the given rectangle to the list.
        - error if the given rectangle already exists, x1 <= x2 or y1 <= y2

    2. Delete a rectangle
        - deletes the rectangle with the given corners
        - error if non-existing rectangle is given

    3. Show all rectangles
        - shows all rectangles in descending order of their area

    4. Show rectangles that intersect a given one
        - select a rectangle from the list of existing rectangle
        - print those which intersect it by descending order of area

    5. exit
        - exit the program

    Observations:
        - Add 10 random rectangles at program startup
        - Write specifications for non-UI functions
        - Each function does one thing only, and communicates via parameters and return value
        - The program reports errors to the user. It must also report errors from non-UI functions!
        - Make sure you understand the rectangle's representation
        - Try to reuse functions across functionalities (Less code to write and test)
        - Don't use global variables!
"""
import random


#
# Write the implementation for Seminar 06 in this file
#

#
# Write below this comment
# Functions to deal with rectangles -- list representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def create_rect(x1, y1, x2, y2: int):
    pass


def equal_rect(rect1, rect2):
    """
    Return True if rect1 and rect2 have he same corners, False otherwise
    :param rect1:
    :param rect2:
    :return:
    """
    pass


#
# Write below this comment
# Functions to deal with rectangles -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


#
# Write below this comment
# Functions that deal with the required functionalities properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def generate_rectangles(count: int):
    rectangles = []

    while count > 0:
        x1 = random.randint(-20, 20)
        y1 = random.randint(-20, 20)
        x2 = x1 + random.randint(1, 10)
        y2 = y1 + random.randint(1, 10)
        new_rect = create_rect(x1, x2, y1, y2)

        # Check for overlapping rectangles
        flag = True
        for rect in rectangles:
            if equal_rect(rect, new_rect) is True:
                flag = False
        if flag:
            rectangles.append(new_rect)
            count -= 1
    return rectangles


print(generate_rectangles(5))

#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

if __name__ == "__main__":
    print("Let's go!")
