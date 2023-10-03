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


def area(rectangle):
    return abs(get_tr_corner(rectangle)[0] - get_bl_corner(rectangle)[0]) * (
            get_tr_corner(rectangle)[1] - get_bl_corner(rectangle)[1])


def intersect(rect1, rect2):
    """
    Return True if and only if the rectangles intersect
    :param rect1: First rectangle
    :param rect2: Second rectangle
    :return:
    """
    # FIXME Replace mock implementation with the real one
    return True


# Moga Denis Andrei
def to_string(rectangle):
    return f"Bottom left corner: {get_bl_corner(rectangle)} -- Top right corner: {get_tr_corner(rectangle)}, area is {area(rectangle)}"


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


# list = generate_rectangles(5)
# for rect in list:
#     print(to_string(rect))


# Moga Denis-Andrei
def check_if_rectangle_exists(rectangle_to_check, list_of_rectangles):
    """

    Args:
        rectangle_to_check (List of tuples): The first rectangle represented as a list with two tuples.
        list_of_rectangles (List of lists): List of lists containing rectangles.

    Returns:
        Boolean value: True if the rectangle already exists, False otherwise.
    """
    for rectangle in list_of_rectangles:
        if equal_rect(rectangle_to_check, rectangle):
            return True

    return False


def add_rectangle_to_list(rectangle, list_of_rectangles):
    if not check_if_rectangle_exists(rectangle, list_of_rectangles):
        # If the rectangle is unique, add it to the list.
        list_of_rectangles.append(rectangle)
        return "ok"

    # Return None if that rectangle already exists in the list.
    return None


#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

def read_number(message):
    number = input(message)
    while not number.isnumeric():
        print("Invalid input! Please enter an integer.")
        number = input(message)
    return int(number)


def read_rectangle():
    x1 = read_number("x1 = ")
    y1 = read_number("y1 = ")
    x2 = read_number("x2 = ")
    y2 = read_number("y2 = ")
    return create_rect(x1, y1, x2, y2)


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


def print_rectangles(rectangles: list):
    for rect in rectangles:
        print(to_string(rect))


def select_rectangle(rectangles):
    """
    User selection of one rectangle
    :param rectangles:
    :return:
    """
    index = 1
    for rect in rectangles:
        print(str(index) + " -> " + to_string(rect))
        index += 1
    selection = read_number("Select rectangle index: ")
    # FIXME Handle case where selection is not a valid index
    return rectangles[selection - 1]


def rect_intersection_ui(rectangles: list):
    # Select a rectangle using the UI
    selected_rect = select_rectangle(rectangles)
    print("Selected rectangle -- " + to_string(selected_rect))

    # Determine intersecting rects
    intersected_rects = []
    for rect in rectangles:
        if intersect(selected_rect, rect) and rect != selected_rect:
            intersected_rects.append(rect)
    # Sort intersected rects by area
    intersected_rects.sort(reverse=True, key=area)
    # Prints them out sorted desc by area
    print_rectangles(intersected_rects)


def printMainMenu():
    print("Mein Menu:")
    print(" 1. Add a rectangle to the list.")
    print(" 2. Delete a rectangle from the list.")
    print(" 3. Show all current rectangles.")
    print(" 4. Select a rectangle to check intersections.")
    print(" 5. Exit.\n")


def main():
    # rectangles = []
    rectangles = generate_rectangles(10)

    while True:
        # clearScreen()
        # print_rectangles(rectangles)
        printMainMenu()
        choice = readNumber("Action: ")
        if choice == 1:
            new_rect = read_rectangle()
            if new_rect is None:
                print("Invalid rectangle (a point or a line are not valid rectangles)")
            else:
                if add_rectangle_to_list(new_rect, rectangles) is None:
                    print("Duplicate rectangle. Cannot be added.")
        elif choice == 2:
            errorMessage("TODO: implement deletion")
        elif choice == 3:
            rectangles.sort(reverse=True, key=area)
            print_rectangles(rectangles)
        elif choice == 4:
            rect_intersection_ui(rectangles)
        elif choice == 5:
            break
        else:
            errorMessage("Unknown choice!")


if __name__ == '__main__':
    main()
