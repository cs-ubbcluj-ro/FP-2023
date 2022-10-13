"""
Let's write a menu-driven application to work with points in 2D space.
    1. Generate points in 2D space
    2. Sort the points by distance from center
    0. Exit
"""
import random

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


def to_str(point):
    """
    Return the point's str representation (e.g., (5,2) => "(x=5, y=2)"
    :param point: Point to represent as str
    :return: The point's str representation
    """
    # TODO Implement me!
    pass


def generate_points():
    """
    1. Ask the user how many points to generate
    2. Generate the points with x,y in [-10,10] and add them to a list (import random -> randint, use create_point)
    3. Print the list of points
    4. Return the list of points
    :return:
    """
    numberOfPoints = int(input("How many points do you want: "))

    list_of_points = []
    for i in range(0, numberOfPoints):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        list_of_points.append(create_point(x, y))
    # TODO Call to_str() when displaying each point
    print(list_of_points)
    return list_of_points


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
