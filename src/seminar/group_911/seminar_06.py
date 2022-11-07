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
    return [x, y, radius]


def get_center(circle):
    return [circle[0], circle[1]]


def get_radius(circle):
    return circle[2]


def to_str(circle):
    """
    Return the circle's representation as a string
    :param circle: The circle
    :return: A string; for circle centered (1,2), radius 4,
    return "circle at (1,2) radius 4"
    """
    return "circle at (" + str(circle[0]) + "," + str(circle[1]) \
           + ") radius " + str(circle[2])


#
# Write below this comment
# Functions to deal with circles -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
# TODO Copy function signatures from list representation and implement them

# circle centered at (1,2) with radius 3 => {"x": 1,"y": 2,"radius": 3}
# def new_circle(x, y, radius: int):
#     return {"x": x, "y": y, "radius": radius}
#
#
# def get_center(circle):
#     return circle.pop("radius")
#
#
# def get_radius(circle):
#     return circle["radius"]
#
#
# def to_str(circle):
#     """
#     Return the circle's representation as a string
#     :param circle: The circle
#     :return: A string; for circle centered (1,2), radius 4,
#     return "circle at (1,2) radius 4"
#     """
#     return "circle at (" + str(circle["x"]) + "," + str(circle["y"]) \
#            + ") radius " + str(circle["radius"])


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


def add_circle(circles_list: list, new_circle):
    """
    Adds the new_circle to the list of circles
    :param circles_list: List of circles maintained by the program
    :param new_circle: The new circle to add
    :return: 0 on success, 1 if circle with given center already exists
    """
    if new_circle in circles_list:
        return 1
    circles_list.append(new_circle)
    return 0


def delete_circle(circles_list: list, circle):
    """
    Deletes a circle from the list of circles
    :param circles_list: List of circles maintained by the program
    :param circle: The circle to delete
    :return: 0 on success, 1 if the circle does not exist
    """
    if circle not in circles_list:
        return 1
    circles_list.remove(circle)
    return 0


#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#
def read_circle(circles_list: list):
    """
    Reads a circle from the console; Circle center must be int X,Y coordinates,
    radius must be > 0 integer (keep reading until true)
    :param circles_list: List of circles maintained by the program.
    :return: The new circle.
    """
    while True:
        print()

        x = input("Enter new X coordinate: ")
        if not x.lstrip('-').isdigit():
            print("X must be an integer.")
            continue
        x = int(x)

        y = input("Enter new Y coordinate: ")
        if not y.lstrip('-').isdigit():
            print("X must be an integer.")
            continue
        y = int(y)

        radius = input("Enter radius (type 0 to stop reading...): ")
        if radius == "0":
            print("Done reading.")
            break
        if not radius.isdigit():
            print("Radius must be an integer greater than 0!")
            continue
        radius = int(radius)

        return new_circle(x, y, radius)


def show_circles(circles_list):
    sorted_list = sorted(circles_list, key=lambda c: get_radius(c), reverse=True)
    print("Current list of circles:\n" + ",\n".join(map(to_str, sorted_list)))


def start():
    # TODO this is the program's entry point
    # What do to here !!!???
    # 1. Print out main menu in a loop
    # 2. Keep the list of circles
    # 3. Call the function corresponding to user choice
    # 4. Print out error messages coming from functions
    circles_list = make_random_circles(10)
    while True:
        print()
        print("Welcome to Circle Manager 9000.")
        print("Please type the number of the operation to execute.")
        print()
        print("1. Add a bunch of circles.")
        print("2. Delete a circle.")
        print()
        print("3. Show a list of circles in descending order of radius.")
        print("4. Show a list of circles which intersect another given circle.")
        print()
        print("5. Exit")
        operation = input()
        if operation == "1":
            circle = read_circle(circles_list)
            exists = add_circle(circles_list, circle)
            if exists:
                print("Circle already exists in the list!")
            else:
                print("OK")
        elif operation == "2":
            circle = read_circle(circles_list)
            not_exists = delete_circle(circles_list, circle)
            if not_exists:
                print("Circle does not exist in the list!")
            else:
                print("OK")
        elif operation == "3":
            show_circles(circles_list)
        elif operation == "4":
            # TODO
            pass
        elif operation == "5":
            print("Goodbye!")
            return
        else:
            print("Unknown operation", operation, "- please try again.")
        # print()
        # print("Press Enter to continue...")
        # input()


if __name__ == "__main__":
    start()
