"""
    Dynamic programming
"""

"""
1. Calculate the maximum subarray sum (subarray = elements having continuous 
indices)

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""

import sys


# sys.maxsize

# Ineficient solution-Dobocan Raul
# An O(n^2) implementation
def max_subarray_sum(array: list):
    if len(array) == 0:
        return None

    maxx = array[0]
    for i in range(0, len(array)):
        sum = 0
        for j in range(i, len(array)):
            sum += array[j]
            if sum >= maxx:
                maxx = sum
    return maxx


# l = [-2, -5, 6, -2, -3, 1, 5, -2]
# print(max_subarray_sum(l))

# Solution with dinamic programming - Enache Vlad
def max_subarray_sum_DP(arr: list):
    if len(arr) == 0:
        return None
    max_ending_here = arr[0]  # initialising the sum with the first element
    max_global = arr[0]
    for i in range(1, len(arr)):
        if arr[i] + max_ending_here < arr[i]:  # the case when we start the sum again
            max_ending_here = arr[i]
        else:  # the case when we continue the sum
            max_ending_here += arr[i]
        max_global = max(max_global, max_ending_here)

    return max_global


# print([-2, -5, 6, -2, -3, 1, 5, -2])

"""
 Maximum subarray divide and conquer - Cirlea Mihai Alexandru

 e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""


# TODO Check this for bugs
def max_subarray_div_conq(arr: list):
    """Uses div and conquer iterative technique to get the max subarray."""
    # Checking for empty arrays
    if not arr:
        return

    stack = [(0, len(arr) - 1)]
    max_sum = arr[0]

    while stack:
        left, right = stack.pop()
        if left == right:
            max_sum = max(arr[left], max_sum)

            # Continue with the next item from the stack
            continue

        middle = (left + right) // 2

        max_left, max_right = arr[left], arr[middle + 1]
        sum_left, sum_right = 0, 0

        # Creating the maximum sum in the left part
        for iterator in range(left, middle + 1):
            if arr[iterator] > sum_left:
                sum_left = arr[iterator]

            else:
                sum_left += arr[iterator]

        max_left = sum_left

        # Creating the maximum sum in the right part
        for iterator in range(middle + 1, right + 1):
            sum_right += arr[iterator]

            if sum_right > max_right:
                max_right = sum_right

        max_sum = max(max_right + max_left, max_sum)

        stack.append((left, middle))
        stack.append((middle + 1, right))

    return max_sum


"""
2. Count in how many ways we can provide change to a given sum of money (N), when provided infinite
   supply of given coin denominations.

   e.g. Let's say N = 10, and we have coins of values (1, 5, 10); we can give change in 4 ways (10, 5 + 5, 5 + 1 + ... 
   and 1 + ... + 1)
"""

"""
3. 0-1 Knapsack problem. Given the weights and values of N items, put them 
    in a knapsack having capacity W so that you
   maximize the value of the stored items. Items cannot be broken up 
   (0-1 property)
"""
W = 11
weights = [1, 2, 3, 4, 7]
values = [1, 5, 8, 3, 2]


def knapsack_01(W: int, weights, values: list, current: int):
    if current == len(weights):
        return 0

    value_include = 0
    if W - weights[current] >= 0:
        value_include = values[current] + knapsack_01(W - weights[current], weights, values, current + 1)
    value_exclude = knapsack_01(W, weights, values, current + 1)

    return max(value_include, value_exclude)


print(knapsack_01(W, weights, values, 0))

"""
4. Gold mine problem (a.k.a checkerboard problem)
   https://www.geeksforgeeks.org/gold-mine-problem
"""
