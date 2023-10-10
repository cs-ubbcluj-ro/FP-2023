"""
What we want to learn today:
    - menu-driven application
    - Python lists and dictionaries (a little bit)
    - manage a list of program entities (circles)
    - how to represent program entities (without classes and objects)
    - divide the program into circle-functions and program functionalities

Problem statement
    A program that manages a list of circles
    A circle has a center (x,y) and a radius (r), r > 0, all ints
        - Add a circle from the console
        - Generate random circles
        - Sort the list by circle radius
        - Exit the program :)
"""
from random import randint


# class my_class:  # class list
#     def method(self, param: int) -> int:
#         return param ** 2
#
#
# x = my_class()
#
# print(x.method(9))
# print(my_class.method(x, 9))

"""
    Circle functions
"""


# we have circle center (1, 3) and radius 2
# as a tuple => (1, 3, 2)
# as a dict => {"x" : 1, "y" : 3, "radius" : 2}
# as a list => [1, 3 , 2]

def create_circle(x: int, y: int, radius: int):
    """
    Create a new circle with given center and radius

    :param x: Center X position
    :param y: Center Y position
    :param radius: Circle radius
    :return: The new circle represented as a Python tuple
    """
    return (x, y, radius)
    # return {"x": x, "y": y, "radius": radius}


def get_radius(c) -> int:
    return c[2]
    # return c["radius"]


def to_str(c) -> str:
    # TODO Write specification for this function
    return "circle center(" + str(c[0]) + "," + str(c[1]) + "), radius=" + str(c[2])
    # return "circle center(" + str(c["x"]) + "," + str(c["y"]) + "), radius=" + str(c["radius"])


c = create_circle(1, 3, 2)

circle_list = [create_circle(1, 3, 2), create_circle(4, 3, 5), create_circle(1, 1, 3)]

# V1 - concat values into an str variable
result = ""
for circle in circle_list:
    result += to_str(circle)
    result += " | "

# print(result[:-2])

# V2 - use the print function
# for circle in circle_list:
#     print(to_str(circle), sep="abcd", end=" | ")

# print(1, 2, 3, 4, 5, 6, sep="|", end="X")

# s = "0123456789"
# print(s[2:])
# print(s[2:5])
# print(s[:5])
# print(s[::2])
# print(s[:-3])

# # old fashioned for loop
# for i in range(0, len(circle_list)):
#     print(to_str(circle_list[i]))

# for i in range():
#     print(i)

# x = range(10 ** 9)

# print(circle_list)

# print(c)
# print(to_str(c))

"""
    Program functionalities
        - Add a circle from the console
        - Generate random circles
        - Sort the list by circle radius
        - Exit the program :)
"""


def sort_circles(data: list) -> None:
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(0, len(data) - 1):
            if get_radius(data[i]) > get_radius(data[i + 1]):
                data[i], data[i + 1] = data[i + 1], data[i]
                # aux = data[i]
                # data[i] = data[i + 1]
                # data[i + 1] = aux
                is_sorted = False


data = [create_circle(1, 3, 2), create_circle(4, 3, 5), create_circle(1, 1, 3)]
while True:
    print("1. Show all circles")
    print("2. Add a random circle")
    print("3. Sort the list by circle radius")
    print("0. Exit")
    opt = input(">")

    if opt == "1":
        for circle in data:
            print(to_str(circle))
    elif opt == "2":
        x = randint(-10, 10)
        y = randint(-10, 10)
        r = randint(1, 6)
        circle = create_circle(x, y, r)
        data.append(circle)

        # append(data, circle)

        # list is a Python class that represents a list
        # list.append is a method defined on class list
        # data is a variable of type list

        # list.append(data,circle)
        # data.append(circle)

        pass
    elif opt == "3":
        sort_circles(data)
    elif opt == "0":
        break
    else:
        print("Invalid input!")
