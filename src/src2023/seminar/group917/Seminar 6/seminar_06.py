#
# Write an application that manages a list of rectangles.
# Each rectangle is represented using its two opposite corners (x1, y1) and (x2, y2)
# The application will have a menu-driven user interface and will provide the following features:
#
#     1. Add a rectangle
#         - adds the given rectangle to the list.
#         - error if the given rectangle already exists, x1 <= x2 or y1 <= y2
#
#     2. Delete a rectangle
#         - deletes the rectangle with the given corners
#         - error if non-existing rectangle is given
#
#     3. Show all rectangles
#         - shows all rectangles in descending order of their area
#
#     4. Show rectangles that intersect a given one
#         - select a rectangle from the list of existing rectangle
#         - print those which intersect it by descending order of area
#
#     5. Show all rectangle sorted in decreasing order of area
#
#     6. exit
#         - exit the program
#
#     Observations:
#         - Add 10 random rectangles at program startup
#         - Write specifications for non-UI functions
#         - Each function does one thing only, and communicates via parameters and return value
#         - The program reports errors to the user. It must also report errors from non-UI functions!
#         - Make sure you understand the rectangle's representation
#         - Try to reuse functions across functionalities (Less code to write and test)
#         - Don't use global variables!
# """
import random
import colorama
from colorama import Fore, Style


# Colorama - can be used to print colorfully in console (pip install colorama in terminal or
# File->Settings->Interpreter->+->search for colorama ->Install)

# Functions that deal with the Rectangle entity
# Everything that needs to be dealt with as far as a Rectangle is concerned
# is done through functions from this section
# We hide details about the representation from the other parts of the app
# Ujfalusi Abel
# Creates a rectangle from 2 coordinates
def create_rectangle(x1: float, y1: float, x2: float, y2: float):
    """

    :param x1: float, x coordinate of first point
    :param y1: float, y coordinate of first point
    :param x2: float, x coordinate of second point
    :param y2: float, y coordinate of second point
    :return: returns a rectangle in a form of a dictionary with 2 tuples representing points
    x1 should not be equal to x2
    y1 should not be equal to y2
    """
    if x1 == x2 or y1 == y2:
        raise ValueError("Coordinates not valid")
    rectangle = {"bottom-left": (min(x1, x2), min(y1, y2)), "top-right": (max(x1, x2), max(y1, y2))}
    return rectangle


# Extracts 4 coordinates in a rectangle
def get_rect_coordinates(rectangle):
    '''

    :param rectangle: a rectangle in the form of a dictionary with 2 tuples containing the coordinates
    :return: 4 float coordinates extracted from the rectangle
    '''
    x1 = rectangle['bottom-left'][0]
    y1 = rectangle['bottom-left'][1]
    x2 = rectangle['top-right'][0]
    y2 = rectangle['top-right'][1]
    return x1, x2, y1, y2


def check_equal(rectangle1, rectangle2):
    """
    Check if two rrectangles are the same
    :param rectangle1:
    :param rectangle2:
    :return: True if they are the same, False otherwise
    """
    x1_1, y1_1, x2_1, y2_1 = get_rect_coordinates(rectangle1)
    x1_2, y1_2, x2_2, y2_2 = get_rect_coordinates(rectangle2)

    if x1_1 == x1_2 and x2_1 == x2_2 and y1_1 == y1_2 and y2_1 == y2_2:
        return True
    return False


# Serban Dragos
def print_menu():
    print("1. Add")
    print("2. Show list of rectangles")
    print("3. Exit")


# Voda Ioan
def verify_if_exist(rectangle_list, rectangle):
    """
    Checks if there exists a rectangle with same coordinates in the list
    :param rectangle_list: the list we are searching
    :param rectangle: the rectangle we are searching
    :return: True if exists, False otherwise
    """
    for curent_rectangle in rectangle_list:
        if check_equal(rectangle, curent_rectangle):
            return True
    return False


def get_bottom_left_point(rectangle):
    """
    Gets coordinates of the point at bottom left corner of the rectangle
    :param rectangle: rectangle for which we need the coordinates
    :return: list of two elements in the form (x,y)
    """
    return rectangle["bottom-left"]


def get_top_right_point(rectangle):
    """
    Gets coordinates of the point at bottom left corner of the rectangle
    :param rectangle: rectangle for which we need the coordinates
    :return: list of two elements in the form (x,y)
    """
    return rectangle["top-right"]


def add_rectangle_to_list(rectangle_list, rectangle):
    """

    :param rectangle_list: list, where we wan t to add
    :param rectangle: ,rectangle who wan t to add
    :return: -; the given list is modified by adding the
            rectangle at the end of the list
    """
    if verify_if_exist(rectangle_list, rectangle):
        raise ValueError("The rectangle already exists.")
    rectangle_list.append(rectangle)


def generate_rectangle_list(n: int) -> list:
    """
    Generate a list of n rectangles with 'random' coordinates
    :param n: the numbers of rectangles to be generated
    :return: the list containing the generated rectangles
            len(list) = n
    """
    rectangle_list = []
    for i in range(n):
        x1 = random.randint(1, 25)
        y1 = random.randint(1, 25)

        x2 = x1 + random.randint(1, 15)
        y2 = y1 + random.randint(1, 15)
        rectangle = create_rectangle(x1, y1, x2, y2)
        add_rectangle_to_list(rectangle_list, rectangle)
    return rectangle_list


def add_ui(rectangle_list):
    """
    Reads the necessary data for creating a Rectangle from the user
    """
    x1 = input("X1=")
    y1 = input("Y1=")
    x2 = input("X2=")
    y2 = input("Y2=")
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)

        rectangle = create_rectangle(x1, y1, x2, y2)
        add_rectangle_to_list(rectangle_list, rectangle)
        print(Fore.GREEN + "SUCCESS: The rectangle was successfully added. " + Style.RESET_ALL)
    except ValueError as e:
        print(Fore.RED + "ERROR: " + str(e) + Style.RESET_ALL)
    # except ZeroDivisionError as e:
    #     print("ERROR:" + str(e))

    # print("This is executed after the try/except block.")


# Serban Dragos
# Serban Dragos
def to_str(rectangle):
    # Current form: I have a chance of messing up the order of
    # my coordinates
    # Helpful: create getter for x1, x2, y1, y2
    # Or at least for the 2 points separately
    x_bottom_left, y_bottom_left = get_bottom_left_point(rectangle)
    x_top_right, y_top_right = get_top_right_point(rectangle)
    return Fore.BLUE + "Point 1 (bottom-left): (" + str(x_bottom_left) + ', ' + str(
        y_bottom_left) + ')' + Style.RESET_ALL + ' | ' + Fore.MAGENTA + "Point 2 (top-right): (" + str(
        x_top_right) + ', ' + str(
        y_top_right) + ')' + Style.RESET_ALL


def show_rectangles(rectangle_list):
    for rectangle_index, rectangle in enumerate(rectangle_list):
        print('Rectangle #' + str(rectangle_index) + ':', to_str(rectangle))


def start():
    rectangle_list = generate_rectangle_list(10)
    while True:
        print_menu()
        option = input("Please choose one of these options: ")
        while not option.isnumeric() or not int(option) in [1, 2, 3]:
            option = input("Please enter a valid value: ")
        option = int(option)
        if option == 1:
            # Adding
            add_ui(rectangle_list)
        if option == 2:
            show_rectangles(rectangle_list)
        if option == 3:
            print("Exiting...")
            break


start()
