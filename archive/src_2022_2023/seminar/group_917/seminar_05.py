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

very_negative_number = -sys.maxsize


# divide & conquer
def max_cross_sum(array: list, left, mid, right: int):
    left_sum = 0
    left_max = -sys.maxsize
    for i in range(mid, left, -1):
        left_sum += array[i]
        left_max = max(left_max, left_sum)

    right_sum = 0
    right_max = -sys.maxsize
    for i in range(mid + 1, right):
        right_sum += array[i]
        right_max = max(right_max, right_sum)
    return left_max + array[mid] + right_max


def max_subarray_sum_dc(array: list, left, right: int):
    if left >= right:
        return array[left]

    mid = (left + right) // 2
    return max(max_subarray_sum_dc(array, left, mid - 1),
               max_subarray_sum_dc(array, mid + 1, right),
               max_cross_sum(array, left, mid, right))


# dynamic programming
def max_subarray_sum(num_list: list):
    if len(num_list) == 0:
        return None
    # Uriesu Iulius
    max_sum = num_list[0]
    current_sum = num_list[0]
    for i in range(1, len(num_list)):
        x = num_list[i]

        current_sum = max(x, current_sum + x)
        # Equivalent to line above
        # if current_sum + x > x:
        #     current_sum += x
        max_sum = max(max_sum, current_sum)
    return max_sum


# Naive implementation
def max_subarry_sum_naive(a: list):
    # Turcu Mihnea
    ans = a[0]
    for i in range(0, len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            ans = max(sum, ans)
    return ans


#
#
# a = [-2, -5, 6, -2, -3, 1, 5, -6]
# print(max_subarry_sum_naive(a))
#
# data = [-2, -5, 6, -2, -3, 1, 5, -6]
# print(max_subarray_sum(data))
#
# print(max_subarray_sum_dc(data, 0, len(data) - 1))

# divide & conquer
# T(n) = 2 * T(n/2) + n => O(n*log_n)

"""
2. Count in how many ways we can provide change to a given sum of money 
(N), when provided infinite
   supply of given coin denominations.

   e.g. Let's say N = 10, and we have coins of values (1, 5, 10); we can 
   give change in 4 ways (10, 5 + 5, 5 + 1 + ... 
   and 1 + ... + 1)
"""

"""
3. 0-1 Knapsack problem. Given the weights and values of N items, put them 
in a knapsack having capacity W so that you
   maximize the value of the stored items. Items cannot be broken up 
   (0-1 property)
"""


def knapsack_01(W: int, weights, values: list, current: int):
    if current == len(weights):
        return 0

    # T(n) = 2 * T(n-1) + 1
    value_include = 0
    if W - weights[current] >= 0:
        value_include = values[current] + knapsack_01(W - weights[current], weights, values, current + 1)
    value_exclude = knapsack_01(W, weights, values, current + 1)

    return max(value_include, value_exclude)


W = 12
weights = [1, 5, 3, 7, 2]
values = [3, 2, 7, 8, 1]

print(knapsack_01(W, weights, values, 0))

"""
4. Gold mine problem (a.k.a checkerboard problem)
   https://www.geeksforgeeks.org/gold-mine-problem
"""
