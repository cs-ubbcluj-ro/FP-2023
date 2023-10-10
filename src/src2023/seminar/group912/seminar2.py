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

"""
    Circle functions
"""


# we have circle center (1, 3) and radius 2
# as a tuple => (1, 3, 2)
# as a dict => {"x" : 1, "y" : 3, "radius" : 2}
# as a list => [1, 3 , 2]

def create_circle(x: int, y: int, radius: int) -> tuple:
    """
    Create a new circle with given center and radius

    :param x: Center X position
    :param y: Center Y position
    :param radius: Circle radius
    :return: The new circle represented as a Python tuple
    """
    return (x, y, radius)


def to_str(c: tuple) -> str:
    # TODO Write specification for this function
    return "circle center(" + str(c[0]) + "," + str(c[1]) + "), radius=" + str(c[2])


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

data = [create_circle(1, 3, 2), create_circle(4, 3, 5), create_circle(1, 1, 3)]
while True:
    print("1. Show all circles")
    print("0. Exit")
    opt = input(">")

    if opt == "1":
        for circle in data:
            print(to_str(circle))
    elif opt == "0":
        break
    else:
        print("Invalid input!")
