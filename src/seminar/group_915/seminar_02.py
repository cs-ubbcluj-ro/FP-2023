"""
Let's write a menu-driven application to work with points in 2D space.
    1. Generate points in 2D space
    2. Sort the points by distance from center
    0. Exit
"""

"""
    Functions for points in 2D
"""


def create_point(x=0, y=0):
    """
    Create a point in 2D space
    :param x: X coordinate
    :param y: Y coordinate
    :return: The created point
    """
    return (x, y)


def generate_points():
    """
    1. Ask the user how many points to generate
    2. Generate the points with x,y in [-10,10] and add them to a list (import random -> randint, use create_point)
    3. Print the list of points
    4. Return the list of points
    :return:
    """
    pass


def start():
    while True:
        print("1. Generate points in 2D space")
        print("2. Sort the points by distance from center")
        print("0. Exit")

        opt = input(">")
        # print(type(opt))

        if opt == "1":
            generate_points()
        elif opt == "2":
            pass
        elif opt == "0":
            return  # or break
        else:
            print("Bad command (or file name) :)")


start()
