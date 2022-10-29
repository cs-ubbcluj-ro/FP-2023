"""
Divide & Conquer

1. Divide => partition problem data into smaller problems of the same type
2. Conquer => solve the "small" problems
3. Combine => rebuild the solution to the original problem

Binary search
 1. Divide => decide in which half to continue the search
 2. Conquer => either find the element, or the element isn't there
 3. Combine => ---

Merge Sort
1. Divide => Divide the list into two halves
2. Conquer => one-element arrays are sorted
3. Combine => merging algorithm

Quick Sort
1. Divide => select pivot, partition, apply for left and right halves
2. Conquer => solve for sublists
3. Combine => --

"""
import random

"""
1. Find the smallest number in a list (chip & conquer, divide in halves, recursive vs non-recursive)
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


def generate_random_array():
    # Uriesu Iulius
    n = random.randint(5, 100)
    num_list = [random.randint(0, 5)]
    for i in range(n - 1):
        num_list.append(num_list[i] + random.randint(1, 5))
    # print(num_list)
    return num_list


# def linear_search(left, right, nr, array):
#     # Richard Toth
#     for i in range(left, right + 1):
#         if array[i] == nr:
#             return True
#     return False
#
#
# def exponential_search(array, nr):
#     # Richard Toth
#     exp = 1
#     if nr == array[0]:
#         return True
#     prevNumber = array[exp]
#     while exp < len(array) and array[exp] < nr:
#         prevNumber = array[exp]
#         exp = exp * 2
#     # if array[exp] == nr:
#     #     return True
#     # exp = exp * 2
#     # if exp > len(array):
#     #     right = len(array) - 1
#     # else:
#     #     right = exp
#     return linear_search(prevNumber, min(exp, len(array) - 1), nr, array)

def binary_search(num_list: list, left: int, right: int, x: int):
    # Uriesu Iulius
    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] == x:
            return mid
        elif num_list[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def exponential_search(num_list: list, x: int):
    # Uriesu Iulius
    n = len(num_list)
    idx = 1
    while idx < n:
        if num_list[idx] == x:
            return idx
        elif num_list[idx] < x:
            idx *= 2
        else:
            return binary_search(num_list, idx // 2, idx, x)
    return binary_search(num_list, idx // 2, n - 1, x)


def test_exponential_search():
    for i in range(1000):
        array = generate_random_array()
        index = random.randint(0, len(array) - 1)
        assert exponential_search(array, array[index]) == index
        assert exponential_search(array, random.randint(-100, -1)) == -1


# test_exponential_search()

"""
3. Calculate the r-th root of a given number x with a given precision p
"""


# TODO Fix for 0 <= x <= 1
def root(left, right, x, r, p):
    mid = (left + right) / 2
    # close enough
    if x - p <= mid ** r <= x + p:
        return mid

    if mid ** r < x - p:
        # search right
        return root(mid, right, x, r, p)
    elif mid ** r > x + p:
        # search left
        return root(left, mid, x, r, p)


# 1.5 ^ 10 < 1.9
# r = 10
# p = 0.000000001
# x = 2
#
# res = root(1, x, x, r, p)
# print(root(1, x, x, r, p))
# print(res ** r)

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
