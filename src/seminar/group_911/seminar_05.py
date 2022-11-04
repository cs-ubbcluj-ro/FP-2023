"""
    Dynamic programming
"""

"""
1. Calculate the maximum subarray sum (subarray = elements having 
continuous indices)
   
    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""
import sys


def max_crossing_sum(array: list, left, mid, right: int):
    left_max = -sys.maxsize
    left_sum = 0

    for i in range(mid, left, -1):
        left_sum += array[i]
        left_max = max(left_max, left_sum)

    right_max = -sys.maxsize
    right_sum = 0

    for i in range(mid + 1, right):
        right_sum += array[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max


def max_subarray_dc(array: list, left, right: int):
    if left >= right:
        return array[left]

    mid = (left + right) // 2

    # T(n) = 2 * T(n/2) + n (looks a lot like merge sort)
    return max(max_subarray_dc(array, left, mid),
               max_subarray_dc(array, mid + 1, right),
               max_crossing_sum(array, left, mid, right))


array = [-2, -5, 6, -2, -3, 1, 5, -6]


# print(max_subarray_dc(array, 0, len(array) - 1))

# import array as arr


def max_subarray_dp(array: list):
    s = 0
    smax = -9999999999999
    init = 1

    # v = arr.array('i', [-2, -5, 6, -2, -3, 1, 5, -6])
    for i in range(0, len(array)):
        # choose whether we extend subarray or start a new one
        # max_here = max(array[i], max_here + array[i])
        # check for new global maximum
        # max_global = max(max_global,max_here)

        s += array[i]
        # check that we have a new maximum
        if s > smax:
            smax = s
        # don't carry over <0 values
        if s < 0:
            s = 0
            init = i + 1
    return smax


# print(max_subarray_dp(array))

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


def knapsack_01(W: int, weights, values: list, current: int):
    if current < 0:
        return 0

    value_include = 0
    if W - weights[current] >= 0:
        value_include = values[current] + knapsack_01(W - weights[current], weights, values, current - 1)
    value_exclude = knapsack_01(W, weights, values, current - 1)

    # T(n) = 2 * T(n-1) + 1
    return max(value_include, value_exclude)


W = 10
weights = [1, 2, 3, 5, 7]
values = [2, 4, 8, 7, 3]
print(knapsack_01(W, weights, values, len(weights) - 1))

"""
4. Gold mine problem (a.k.a checkerboard problem)
   https://www.geeksforgeeks.org/gold-mine-problem
"""
