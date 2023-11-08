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

    5. Show all rectangle sorted in decreasing order of area

    6. exit
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
    Functions that represent rectangles
        - functions here know how a rectangle is represented 
        - functions here do not use input/print and do not talk to the user
        - lowest level
"""


# (x1,y1) - (x2,y2)

# rectangle as a tuple of tuples
# (1, 2), (4, 3) -> ((1, 2), (4, 3))

# rectangle as a dictionary
# (1, 2), (4, 3) -> {"x1" : 1, "y1": 2, "x2": 4, "y2": 3}

def create_rect(x1: int, y1: int, x2: int, y2: int):
    """
    Ways to validate the returned type
        1. Return empty tuple -- problem is that caller needs to check the returned value explicitly
        2. throw an Error -- should be checked
    """
    if x1 == x2 or y1 == y2:
        raise ValueError("Invalid corners for rectangle")

    # return {"x1": min(x1, x2), "y1": min(y1, y2), "x2": max(x1, x2), "y2": max(y1, y2)}
    return ((min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2)))


def equal(r1, r2) -> bool:
    # TODO This only works due to the dict, tuple or list implementation
    return r1 == r2


def get_width(r) -> int:
    return r[1][0] - r[0][0]


def get_height(r) -> int:
    return r[1][1] - r[0][1]


def area(r) -> int:
    return get_width(r) * get_height(r)


def to_str(rect) -> str:
    # return "Rectangle " + str((rect["x1"], rect["y1"])) + ", " + str((rect["x2"], rect["y2"]))
    return "Rectangle " + str(rect[0]) + ", " + str(rect[1]) + ", area=" + str(area(rect))


"""
    Functions that implement program functionalities
        - use the functions defined above
        - functions here do not use input/print and do not talk to the user
        - mid-level :)  
"""


def generate_rectangles(n: int) -> list:
    """
    Generate n pseudo-random rectangles
    :param n: Number of rectangles to generate
    :return: The list
    """
    result = []

    while n > 0:
        x1 = randint(0, 100)
        y1 = randint(0, 100)
        x2 = x1 + randint(1, 100)
        y2 = y1 + randint(1, 100)
        result.append(create_rect(x1, y1, x2, y2))
        n -= 1

    return result


"""
    User interface
        - all input() / print() calls must be here
        - the only part that communicates with the user directly
        - calls functions defined in the sections above
        
    
    functions in <User interface> --> functions in <program functionalities> --> function in <rectangle representation>
"""


def read_rectangle():
    print("Reading rectangle")
    x1 = int(input("X1="))
    y1 = int(input("Y1="))
    x2 = int(input("X2="))
    y2 = int(input("Y2="))
    return create_rect(x1, y1, x2, y2)


def add_rectangle_ui(data: list):
    """
    1. Read the rect from the keyboard
    2. Add it to the list
    """
    try:
        r = read_rectangle()

        for rect in data:
            if equal(r, rect):
                print("Duplicate rectangle")
                return
        data.append(r)
    except ValueError as ve:
        print("Error reading rectangle " + str(ve))


def show_sorted_by_area(data: list) -> None:
    # sorted_list = sorted(data,reverse=True)
    print("List of rectangles sorted by area:")
    for r in sorted(data, key=area, reverse=True):
        print(to_str(r))


def start():
    data = generate_rectangles(10)

    while True:
        # main program loop
        print("1. Show all rectangles")
        print("2. Add rectangle")
        print("3. Show all rectangles sorted by area")
        print("0. Exit")

        option = input(">")

        if option == "1":
            print("List of rectangles:")
            for r in data:
                print(to_str(r))
        elif option == "2":
            add_rectangle_ui(data)
        elif option == "3":
            show_sorted_by_area(data)
        elif option == "0":
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    start()
