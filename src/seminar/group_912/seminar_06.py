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
# def create_rect(x1, y1, x2, y2: int):
#     """
#     Create a rectangle with corners (x1, y1) and (x2, y2).
#     :param x1:
#     :param y1:
#     :param x2:
#     :param y2:
#     :return: The newly created rectangle
#     """
#     pass


# def rect_equal(rect1, rect2):
#     """
#     Return True iff the two rectangles are equal (have the same corners)
#     :param rect1:
#     :param rect2:
#     :return:
#     """
#     pass


#
# Write below this comment
# Functions to deal with rectangles -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
# Dumitrana Mihnea dictionary repres.
def create_rect(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return None

    rect = {}
    rect['low_left'] = (min(x1, x2), min(y1, y2))
    rect['up_right'] = (max(x1, x2), max(y1, y2))
    return rect


def get_x1(rect):
    return rect["low_left"][0]


def get_y1(rect):
    return rect["low_left"][1]


def get_x2(rect):
    return rect["up_right"][0]


def get_y2(rect):
    return rect["up_right"][1]


def rect_equal(rect1, rect2: dict):
    return get_x1(rect1) == get_x1(rect2) and get_x2(rect1) == get_x2(rect2) and get_y1(rect1) == get_y1(
        rect2) and get_y2(rect1) == get_y2(rect2)


def to_str(rect):
    return "{} {} | {} {}".format(get_x1(rect), get_y1(rect), get_x2(rect), get_y2(rect))


#
# Write below this comment
# Functions that deal with the required functionalities properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def gen_rectangles(count: int):
    result = []
    while count > 0:
        x1 = random.randint(-20, 20)
        y1 = random.randint(-20, 20)
        x2 = x1 + random.randint(1, 10)
        y2 = y1 + random.randint(1, 10)

        new_rect = create_rect(x1, y1, x2, y2)
        rect_ok_flag = True
        for rect in result:
            if rect_equal(new_rect, rect):
                rect_ok_flag = False
                break
        if rect_ok_flag:
            result.append(new_rect)
            count -= 1

    return result


# rects = gen_rectangles(5)
# print(rects)

def add_rectangle(rectangles: list, new_rect):
    """
    :param rectangles: list
    :param x1,x2,y1,y2: int
    :return:
        None if rectangle already exists or is invalid
        updated list if rectangle is ok
    """
    # newRectangle = [x1, y1, x2, y2]
    # newRectangle = create_rect()
    # if x1 > x2 or y1 > y2:
    #     return None
    for rectangle in rectangles:
        if rect_equal(rectangle, new_rect):
            return None

    rectangles.append(new_rect)
    return rectangles


#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

def show_all_rect(rect_list: list):
    print("Rectangle list:")
    for rect in rect_list:
        print(to_str(rect))


# Chisleac Remus
def read_rect_ui():
    x1 = int(input("x1="))
    y1 = int(input("y1="))
    x2 = int(input("x2="))
    y2 = int(input("y2="))

    return create_rect(x1, y1, x2, y2)


def add_rectangle_ui(rectangles: list):
    new_rect = read_rect_ui()
    if new_rect is None:
        print("Invalid rectangle. Cannot be added")
        return

    if add_rectangle(rectangles, new_rect) is None:
        print("Overlapping rectangles. Rectangle was not added.")


def start_menu():
    rectangles = gen_rectangles(1)
    while True:
        show_all_rect(rectangles)
        print(rectangles)
        print("1. Add a rectangle:\n",
              "2. Delete a rectangle:\n",
              "3. Show all rectangles:\n",
              "4. Show rectangles that intersect a given one:\n",
              "5. exit\n")
        opt = input('>')
        if opt == "1":
            add_rectangle_ui(rectangles)
        elif opt == "2":
            pass
        elif opt == "3":
            pass
        elif opt == "4":
            pass
        elif opt == "5":
            return
        else:
            print("Choose a valid option")
        # Dumitrescu David


if __name__ == "__main__":
    start_menu()
