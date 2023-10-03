"""
Rational number as list
"""

def create_q(num, den: int = 1):
    """
    Create Rational number
    :param num:
    :param den:
    :return: The number, or None if number is invalid
    """
    if den == 0:
        raise ValueError("denominator cannot be 0")
    return [num, den]
    # return {"num": num, "den": den}


def get_num(q):
    return q[0]
    # return q["num"]


def get_den(q):
    return q[1]
    # return q["den"]