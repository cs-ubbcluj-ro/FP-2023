"""
We want to get some practice with:
    1. Python 3
    2. Writing a menu-driven console application
    3. Generating some numbers :)
    4. Representing program entities

Let's implement something - Manage a list of rational numbers
    Functionalities:
        1. Add a new rational number from console
        2. Adding some random numbers programmatically
        3. Sort the list of numbers
        4. Exit the program
"""


# Functions for rational numbers
# create a number, compare 2 numbers

# Data type recap: int, float, boolean, str, tuple, list, dict
# we keep the numbers in a Python list
# we represent each number as a dict

def create_q(num: int, den: int) -> dict:
    """
    Create a new rational number
    :param num: numerator value
    :param den: denominator value
    :return: the newly created number
    """
    return {"num": num, "den": den}


def to_str(q: dict) -> str:
    """
    Return the number's string representation
    :param q: The rational number
    :return: str representation
    """
    return str(q["num"]) + "/" + str(q["den"])


print(create_q(1, 4))
print(to_str(create_q(1, 4)))

# Program functionalities

data = [create_q(1, 2), create_q(2, 3), create_q(4, 5)]
print(data)

for i in range(0, len(data)):
    print(to_str(data[i]))

for q in data:
    print(to_str(q))
