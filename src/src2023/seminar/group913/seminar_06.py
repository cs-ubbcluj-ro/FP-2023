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
from random import randint

"""
    Rectangle functions
    - the only place where we have to know the rectangle's actual representation
    - the only place where it matters if the rectagle is represented as a list or 
      as a dictionary
"""


def create_rect(x1: int, y1: int, x2: int, y2: int):
    """
    Create and return a rectangle with (x1,y1) and (x2,y2) corners
    :return: The newly created rectangle
    Raise ValueError in case points cannot form a rectangle
    """
    # (x1, y1) and (x2, y2) are opposing corners
    if x1 == x2 or y1 == y2:
        # a point or a line, not a "real" rectangle
        # None is the error code
        # return None
        raise ValueError("Coordinates do not form a rectangle")

    # dict implementation for rectangle
    return {"X1": min(x1, x2), "Y1": min(y1, y2), "X2": max(x1, x2), "Y2": max(y1, y2)}

    # list implementation for rectangle
    # return [(min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2))]
    # return [x1, y1, x2, y2]


def get_bottom_left(rect) -> tuple:
    return rect["X1"], rect["Y1"]
    # return rect[0]


def get_top_right(rect) -> tuple:
    return rect["X2"], rect["Y2"]
    # return rect[1]


def to_str(rect) -> str:
    # return min(rect.keys())
    # tuple unpacking
    x1, y1 = get_bottom_left(rect)
    x2, y2 = get_top_right(rect)

    return ("(" + str(x1) + "," + str(y1) + ") - (" +
            str(x2) + "," + str(y2) + ")")


"""
    Program functionalities
"""


def generate_rectangles(n: int) -> list:
    """
    Generate n pseudo-random rectangles
    :param n: How many rectangles to generate
    :return: The list of rectangles
    """
    result = []

    while n > 0:
        x1 = randint(1, 20)
        y1 = randint(1, 20)
        x2 = x1 + randint(1, 20)
        y2 = y1 + randint(1, 20)
        result.append(create_rect(x1, y1, x2, y2))
        n -= 1
    return result


"""
    User interface
    - only place where print/input are allowed
"""


def add_rectangle_ui(rectangles: list):
    print("2", id(rectangles))
    """
    Add a new rectangle to the list
    :return: None
    """
    try:
        """
        Order of operations in the line below
        1. input() is called
        2. int() is called on whatever was returned by input()
        3. assignment to x1 variable
        """
        x1 = int(input("X1="))
        y1 = int(input("Y1="))
        x2 = int(input("X2="))
        y2 = int(input("Y2="))
    except ValueError as ve:
        print("Error reading coordinates - " + str(ve))
        return

    r = create_rect(x1, y1, x2, y2)


    # list.append(rectangles,r)
    rectangles.append(r)
    rectangles.clear()
    # new address, new type, new value
    print("3", id(rectangles))


def print_menu():
    print("1. Show all rectangles")
    print("2. Add a rectangle")
    print("0. Exit")


def start():
    # rectangles -- local variable to start() function
    rectangles = generate_rectangles(10)

    while True:
        print_menu()
        opt = input(">").strip()
        if opt == "1":
            for r in rectangles:
                print(to_str(r))
        elif opt == "2":
            print("1", id(rectangles))
            add_rectangle_ui(rectangles)
            print("4", id(rectangles))
        elif opt == "0":
            print("bye!")
            exit(0)
            # return
        else:
            print("Invalid input")


if __name__ == "__main__":
    # try:
    #     """
    #     order of operations
    #         1. create_rect is called
    #         2. create_rect returns a value
    #         3. value is assigned to variable r, which is now initialized
    #         in case create_rect raises and exception, 2 and 3 do not take place!
    #     """
    #     r = create_rect(1, 1, 1, 3)
    #
    #     """
    #     if create_rect raised and exception, the below never runs
    #     """
    #     # print(r)
    # except ValueError as ve:
    #     print(ve)

    start()
