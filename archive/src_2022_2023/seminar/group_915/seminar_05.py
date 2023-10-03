"""
    Dynamic programming
"""

"""
1. Calculate the maximum subarray sum (subarray = elements having continuous 
indices)

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""


def max_subarray_sum(array: list):
    if len(array) == 0:
        return None

    max_global = array[0]
    max_ending_here = array[0]
    for i in range(1, len(array)):
        max_ending_here = max(array[i], array[i] + max_ending_here)
        # if array[i] + max_ending_here > array[i]:
        #     max_ending_here += array[i]
        # else:
        #     ...
        max_global = max(max_global, max_ending_here)
    return max_global


# data = [-2, -5, 6, -2, -3, 1, 5, -6]
# # data = [-10, -2, -3]
# print(max_subarray_sum(data))

"""
2. Count in how many ways we can provide change to a given sum of money (N), 
    when provided infinite  supply of given coin denominations.

   e.g. Let's say N = 10, and we have coins of values (1, 5, 10); 
   we can give change in 4 ways (10, 5 + 5, 5 + 1 + ... and 1 + ... + 1)
"""

"""
3. 0-1 Knapsack problem. Given the weights and values of N items, put them in 
a knapsack having capacity W so that you
   maximize the value of the stored items. Items cannot be broken up 
   (0-1 property)
"""
weights = [1, 3, 7, 2, 5]
values = [2, 4, 9, 10, 1]
W = 12


def knapsack_01(W: int, weights, values: list, current: int):
    if current < 0:
        return 0

    value_include = 0
    if W - weights[current] >= 0:
        value_include = values[current] + knapsack_01(W - weights[current], weights, values, current - 1)
    value_exclude = knapsack_01(W, weights, values, current - 1)
    return max(value_include, value_exclude)


print(knapsack_01(W, weights, values, len(weights) - 1))

"""
4. Gold mine problem (a.k.a checkerboard problem)
   https://www.geeksforgeeks.org/gold-mine-problem
"""
