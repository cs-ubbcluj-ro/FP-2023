"""
Let's write a menu-driven application to work with points in 2D space.
    1. Generate points in 2D space
    2. Sort the points by distance from center
    0. Exit
"""
import math
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
    return {"x": x, "y": y}
    # return (x, y)


def get_x(p):
    return p["x"]


def get_y(p):
    return p["y"]


def to_str(point):
    """
    Return the point's str representation (e.g., (5,2) => "(x=5, y=2)")
    :param point: Point to represent as str
    :return: The point's str representation
    """
    return "x=" + str(get_x(point)) + ", y=" + str(get_y(point))
    # return f"x={point[0]}, y={point[1]}"


def distance_center(point):
    """
    Return the Euclidean distance between the point and (0,0)
    :param point:
    :return: The distance as a float
    """
    x = get_x(point)
    y = get_y(point)

    return math.sqrt(x * x + y * y)


def sort_points(point_list):
    """
    Sort the points by distance to center
    :param point_list: The list of points
    :return: The sorted list of points
    """
    point_list.sort(key=distance_center)

    for p in point_list:
        print(to_str(p))
    return point_list


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

    # print(list_of_points)
    for p in list_of_points:
        print(to_str(p))
    return list_of_points


def start():
    point_list = []
    while True:
        print("1. Generate points in 2D space")
        print("2. Sort the points by distance from center")
        print("0. Exit")

        opt = input(">")
        # print(type(opt))

        if opt == "1":
            point_list = generate_points()
        elif opt == "2":
            point_list = sort_points(point_list)
        elif opt == "0":
            return  # or break
        else:
            print("Bad command (or file name) :)")


start()

"""
def add(a, b):
    return a + b


x = add

print(type(x))
print(x(3, 4,5))
"""
