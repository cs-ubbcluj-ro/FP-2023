"""
Write an application that manages a list of circles.
Each circle has a unique center (x,y - ints) and a positive radius (int).
The application will have a menu-driven user interface and will provide the following features:

    1. Add a circle
        - adds the given circle to the list.
        - error if circle with given center already exists, the center
        or radius not given, empty or radius < 0

    2. Delete a circle
        - deletes the circle with the given center
        - error if non-existing center is given

    3. Show all circles
        - shows all circles in descending order of their radius

    4. Show circles that intersect a given one
        - select a circle from the list of existing circles
        - print those which intersect it
        (bonus: sort printed circles by descending order of radius)

    5. exit
        - exit the program

    Observations:
        - Add 10 random circles at program startup
        - Write specifications for non-UI functions
        - Each function does one thing only, and communicates via parameters and return value
        - The program reports errors to the user. It must also report errors from non-UI functions!
        - Make sure you understand the circle's representation
        - Try to reuse functions across functionalities (Less code to write and test)
        - Don't use global variables!
"""
import random


#
# Write the implementation for Seminar 06 in this file
#

#
# Write below this comment
# Functions to deal with circles -- list representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

# circle centered at (1,2) with radius 3 => [1, 2, 3]
def new_circle(x, y, radius: int):
    pass


def get_center(circle):
    pass


def get_radius(circle):
    pass


def to_str(circle):
    """
    Return the circle's representation as a string
    :param circle: The circle
    :return: A string; for circle centered (1,2), radius 4,
    return "circle at (1,2) radius 4"
    """
    pass


#
# Write below this comment
# Functions to deal with circles -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
# TODO Copy function signatures from list representation and implement them

# circle centered at (1,2) with radius 3 => {"x": 1,"y": 2,"radius": 3}

#
# Write below this comment
# Functions that deal with the required functionalities properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def make_random_circles(count: int):
    """
    Create count random circles
    :return: The list of newly created circles
    """
    assert count < 40 ** 2

    circles_list = []
    centers_x = list(range(-20, 20))
    centers_y = list(range(-20, 20))

    while count > 0:
        x = random.choice(centers_x)
        y = random.choice(centers_y)
        centers_x.remove(x)
        centers_y.remove(y)
        radius = random.randint(1, 20)
        circles_list.append(new_circle(x, y, radius))
        count -= 1
    return circles_list


circ = make_random_circles(5)


def add_circle(circles_list: list, new_circle):
    """
    Adds the new_circle to the list of circles
    :param circles_list: List of circles maintained by the program
    :param new_circle: The new circle to add
    :return: 0 on success, 1 if circle with given center already exists
    """
    pass


#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#
def read_circle():
    """
    Reads a circle from the console; Circle center must be int X,Y coordinates,
    radius must be > 0 integer (keep reading until true)
    :return: The new circle.
    """
    pass


def start():
    # TODO this is the program's entry point
    # What do to here !!!???
    # 1. Print out main menu in a loop
    # 2. Keep the list of circles
    # 3. Call the function corresponding to user choice
    # 4. Print out error messages coming from functions
    pass


if __name__ == "__main__":
    start()
