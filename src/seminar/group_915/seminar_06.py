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
import os
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
import time


def create_rect(x1, y1, x2, y2: int):
    """
        This function creates a rectangle using the coordinates of two opposing corners.

    Args:
        x1 (_type_): _description_
        y1 (_type_): _description_
        x2 (_type_): _description_
        y2 (_type_): _description_
    """
    if x1 == x2 or y1 == y2:
        # A point or line is not a valid rectangle
        return None

    # bottom-left rectangle corner
    bl = (min(x1, x2), min(y1, y2))
    # top right rectangle corner
    tr = (max(x1, x2), max(y1, y2))
    return [bl, tr]


def get_tr_corner(rect):
    return rect[1]


def get_bl_corner(rect):
    return rect[0]


def equal_rect(rect1, rect2):
    return rect1 == rect2
    # return not (get_tr_corner(rect1) != get_tr_corner(rect2) or get_bl_corner(rect1) != get_bl_corner(rect2))


# Moga Denis Andrei
def to_string(rectangle):
    return f"Bottom left corner: {get_bl_corner(rectangle)} -- Top right corner: {get_tr_corner(rectangle)}"


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
        new_rect = create_rect(x1, y1, x2, y2)

        # Check for overlapping rectangles
        flag = True
        for rect in rectangles:
            if equal_rect(rect, new_rect) is True:
                flag = False
        if flag:
            rectangles.append(new_rect)
            count -= 1
    return rectangles


list = generate_rectangles(5)
for rect in list:
    print(to_string(rect))


#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

# Oniga Andrei Mihai
def clearScreen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def errorMessage(message):
    # clearScreen()
    print(f"\n{message}\nGoing back to where you were before...")
    # time.sleep(2)


def readNumber(message):
    try:
        val = int(input(message))
        return val
    except:
        errorMessage("A number is expected.")
        return 0


def printMainMenu():
    print("Mein Menu:")
    print(" 1. Add a rectangle to the list.")
    print(" 2. Delete a rectangle from the list.")
    print(" 3. Show all current rectangles.")
    print(" 4. Select a rectangle to check intersections.")
    print(" 5. Exit.\n")


def main():
    while True:
        # clearScreen()
        printMainMenu()
        choice = readNumber("Action: ")
        if choice == 1:
            errorMessage("TODO: implement addition")
        elif choice == 2:
            errorMessage("TODO: implement deletion")
        elif choice == 3:
            errorMessage("TODO: implement showing")
        elif choice == 4:
            errorMessage("TODO: implement intersections")
        elif choice == 5:
            break
        else:
            errorMessage("Unknown choice!")


if __name__ == '__main__':
    main()
