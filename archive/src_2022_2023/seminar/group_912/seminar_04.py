"""
    Divide & Conquer + Combine (the results of the small, already solved subproblems
"""
import random

"""
1. Find the smallest number in a list (chip & conquer, divide in halves, recursive vs non-recursive). Return None for
    an empty list
    a. Chip & conquer, recursive
    b. Divide in halves, non-recursive
    c. Divide in halves, recursive
"""


# a. Chip & conquer, recursive
def array_min_impl(array: list, start_index: int):
    if start_index == len(array) - 1:
        return array[start_index]
    return min(array_min_impl(array, start_index + 1), array[start_index])


def array_min(array: list):
    if len(array) == 0:
        return None
    return array_min_impl(array, 0)


# b. Divide in halves, non-recursive
def divide_in_halves_iter(my_list: list):
    """Returns the smallest number from a list"""
    if not len(my_list):
        return None

    min_found = my_list[0]
    stack = [(0, len(my_list) - 1)]

    # As long as we have elements in the stack
    while len(stack):
        left, right = stack.pop()
        if left == right:
            min_found = min(my_list[left], min_found)

            # Then we continue with the next item from the stack
            continue

        # If we got to this point, it means left != right
        mid = (left + right) // 2

        # We look in the first half
        stack.append((left, mid))

        # We look in the second half
        stack.append((mid + 1, right))

    return min_found


# c. Divide in halves, recursive
def calc_array_min_impl(array: list, left, right: int):
    if right == left:
        return array[left]
    mid = (left + right) // 2
    return min(calc_array_min_impl(array, left, mid), calc_array_min_impl(array, mid + 1, right))


def calc_array_min(array: list):
    if len(array) == 0:
        return None
    return calc_array_min_impl(array, 0, len(array) - 1)


# def test_divide():
#     for count in range(1000):
#         length = random.randint(1, 100)
#         array = []
#         for i in range(length):
#             array.append(random.randint(-100, 100))
#         assert calc_array_min(array) == min(array), (calc_array_min(array), array)
#         assert array_min(array) == min(array), (array_min(array), array)
#         assert divide_in_halves_iter(array) == min(array), (divide_in_halves_iter(array), array)
#     # special case - empty array
#     assert calc_array_min([]) is None
#     assert array_min([]) is None
#     assert divide_in_halves_iter([]) is None
#
#
# test_divide()

"""
2. Exponential search
    a. Generate a pseudo-random array of increasing elements
    b. Implement exponential search
    c. Implement binary search
    d. Driver & test functions
"""


def generate_random_increasing_array():
    # n=length of array
    n = random.randint(0, 100)
    array = [random.randint(0, 100)]
    for i_ul in range(1, n):
        array.append(array[i_ul - 1] + random.randint(0, 2))
    return array


def exponential_search(array: list, key: int):
    poz = 1
    while poz <= len(array) - 1 and array[poz] < key:
        poz *= 2

    # TODO Replace the linear search with binary search
    for i in range(poz // 2, min(poz + 1, len(array))):
        if array[i] == key:
            return i
    return -1


# def test_exponential_search():
#     for i in range(1000):
#         array = generate_random_increasing_array()
#         pos = random.randint(0, len(array) - 1)
#
#         # array[...] as array the array is not strictly increasing
#         assert array[exponential_search(array, array[pos])] == array[pos], (pos, array, array[pos])


# test_exponential_search()

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
