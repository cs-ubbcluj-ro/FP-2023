"""
    Problem Solving Methods -- Divide & Conquer and Backtracking
"""
from random import randint

"""
1. Find the smallest number in a list (chip & conquer, divide in halves, recursive vs non-recursive). Return None for
    an empty list
    a. Chip & conquer, recursive
    b. Divide in halves, non-recursive
    c. Divide in halves, recursive
"""

"""
2. Exponential search
    a. Generate a pseudo-random array of increasing elements
    b. Implement exponential search
    c. Implement binary search
    d. Driver & test functions
"""


# Rares Cotoi
# Costea Razvan
def generate_list(n: int) -> list:
    """
       Generate a list of n integers sorted ascending
       :param n: Length of the list
       :return: The list of numbers
       """
    x = randint(0, 100)
    list = []
    list.append(x)
    for i in range(1, n):
        x = x + randint(1, 100)
        list.append(x)
    return list


def test_search():
    """
    Function that generates 1000 lists and tests the implementation of exponential search
    on them

    Use assert to make the actual check
    :return:
    """
    for i in range(1_000):
        data = generate_list(randint(1, 1_000))
        elem = data[0] - randint(1, 100)  # this element is NOT in the list
        assert exponential_search(data, elem) == -1
        elem = data[-1] + randint(1, 100)  # this element is NOT in the list
        assert exponential_search(data, elem) == -1

        # check that exponential search finds all elements in the list
        # FIXME what happens in case of list duplicates?
        for i in range(len(data)):
            assert exponential_search(data, data[i]) == i


def binary_search(data: list, key: int, left: int, right: int) -> int:
    """
    Binary search for key between bounds left and right. Return -1 if key not found
    :return: Key index or -1 if not found
    """
    if right >= left:
        mid = left + (right - left) // 2

        if data[mid] == key:
            return mid
        elif key < data[mid]:
            return binary_search(data, key, left, mid - 1)
        else:
            return binary_search(data, key, mid + 1, right)
    else:
        return -1


def exponential_search(data: list, key: int) -> int:
    """
    Exponential search in an ascending sorted list.
    :param data: The list
    :param key: The searched key
    :return: Lowest index where the key is found, or -1 if key not in the list
    """
    if data[0] > key or data[-1] < key:
        return -1

    length = len(data)

    if data[0] == key:
        return 0

    idx = 1

    while idx < length and data[idx] <= key:
        idx *= 2

    return binary_search(data, key, idx // 2, min(idx, length - 1))


# test_search()

"""
3. Calculate the r-th root of a given number x with a given precision p
"""


def root(root_power: float, number: int, precision: float) -> float:
    """
    Compute the n-th root of a number with a given precision
    :param root_power: The root
    :param number: The number to find the root of
    :param precision: The precision
    :return: The root
    """
    left = 0.0
    right = number ** root_power

    while abs(right - left) > precision:
        mid = (left + right) / 2
        mid_power = mid ** root_power

        if mid_power < number:
            left = mid
            right *= 2
        elif mid_power > number:
            right = mid
        else:
            return mid

    return (left + right) / 2


print(root(8, 2, 0.0001))
print(2 ** 0.125)

"""
4. Calculate the maximum subarray sum (subarray = elements having continuous indices)
    a. Naive implementation
    b. Divide & conquer implementation

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""

"""
    Backtracking
"""

"""
5. Recursive implementation for permutations
"""


def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """
    return len(set(x)) == len(x)


def solution(x, n):
    """
    Determines whether we have a solution
    """
    return len(x) == n


def solution_found(x):
    """
    What to do when a solution is found
    """
    print("Solution: ", x)


def bkt_rec(x, n):
    """
    Backtracking algorithm for permutations problem, recursive implementation
    """
    x.append(0)
    for i in range(0, n):
        x[len(x) - 1] = i
        if consistent(x):
            if solution(x, n):
                solution_found(x)
            else:
                bkt_rec(x[:], n)


"""
    What's important to know about backtracking!
        1. Search space representation (what and how we represent in array X)
        2. Check that array X is consistent (consistent <=> might it be possible to reach a
        solution by only adding values to array X?)
        3. Check that array X represents a solution to the problem
        
        permutations of 4 ( 1, 2, 3, 4)
        X = [ 1 3 2 4
        
"""
bkt_rec([], 4)

"""
6. Change the code for generating the permutation above to work for the n-Queen problem
"""

"""
A Latin square is an n × n square filled with n different symbols, each occurring exactly once in each row and exactly 
once in each column

7. Generate all the N x N Latin squares for a given number N. 

8. Generate all reduced N x N Latin squares for a given number N. In a reduced Latin square, the elements of the first 
row and column are sorted.
"""
