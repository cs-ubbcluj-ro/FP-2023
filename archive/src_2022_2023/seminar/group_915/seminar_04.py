"""
    Divide & Conquer
"""
import random

"""
1. Find the smallest number in a list (chip & conquer, divide in halves, recursive vs non-recursive)
    a. Chip & conquer, recursive
    b. Divide in halves, non-recursive
    c. Divide in halves, recursive
"""


# a. Chip & conquer, recursive
def one_chip_conquer(array: list, left: int):
    if left == len(array) - 1:
        return array[left]
    return min(array[left], one_chip_conquer(array, left + 1))


def min_array_chip_conquer(array: list):
    if len(array) == 0:
        return None
    return one_chip_conquer(array, 0)


# b. Divide in halves, non-recursive
def smallest_num_iter(data: list):
    if len(data) == 0:
        return None
    stack = [(0, len(data) - 1)]
    min_value = data[0]  # sys.maxvalue

    while len(stack) > 0:
        left, right = stack.pop()

        if left == right:
            min_value = min(min_value, data[left])
        else:
            mid = (left + right) // 2
            stack.append((left, mid))
            stack.append((mid + 1, right))

    return min_value


# c. Divide in halves, recursive
def smallest_num_rec_impl(data: list, left, right: int):
    if len(data) == 0:
        return None

    if left == right:
        return data[left]

    mid = (left + right) // 2

    return min(smallest_num_rec_impl(data, left, mid), smallest_num_rec_impl(data, mid + 1, right))


def smallest_num_rec(data: list):
    return smallest_num_rec_impl(data, 0, len(data) - 1)


def test_min_array():
    for i in range(1000):
        length = random.randint(1, 100)
        array = []
        for i in range(length):
            array.append(random.randint(-10, 10))

        assert min_array_chip_conquer(array) == min(array), array
        assert smallest_num_iter(array) == min(array), array
        assert smallest_num_rec(array) == min(array), array
    assert min_array_chip_conquer([]) is None, "Empty array"
    assert smallest_num_iter([]) is None, array
    assert smallest_num_rec([]) is None, "Empty array"


# test_min_array()

"""
2. Exponential search
    a. Generate a pseudo-random array of increasing elements
    b. Implement exponential search
    c. Implement binary search
    d. Driver & test functions
"""


def generate_pseudo_random_array():
    array = [random.randint(0, 10)]
    for i in range(1, random.randint(1, 20)):
        array.append(random.randint(array[i - 1] + 0, array[i - 1] + 2))
    return array


# Moga - I implemented expo search and binary search
def exponential_search(array: list, key: int):
    prev_pos = 0
    next_pos = 1

    while next_pos < len(array) and array[next_pos] < key:
        prev_pos = next_pos
        next_pos *= 2

    if next_pos >= len(array):
        next_pos = len(array) - 1

    # This returns the bounds between the value key is found...
    for i in range(prev_pos, next_pos + 1):
        if array[i] == key:
            return i
    return None


# TODO Integrate into exponential search
def binary_search(data, left, right, key):
    mid = (left + right) // 2
    if data[mid] == key:
        return mid
    elif data[mid] <= key:
        return binary_search(data, mid + 1, right, key)
    return binary_search(data, left, mid - 1, key)


def test_exponential_search():
    for i in range(1000):
        # Only cases where the element must be found
        array = generate_pseudo_random_array()
        key_pos = random.randint(0, len(array) - 1)

        assert array[exponential_search(array, array[key_pos])] == array[key_pos], (
            exponential_search(array, array[key_pos]), key_pos, array)
        # TODO Implement test cases for elements not in the array


test_exponential_search()

"""
3. Calculate the r-th root of a given number x with a given precision p
"""

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


# bkt_rec([], 4)

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
