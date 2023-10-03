"""
Created on Jan 6, 2017

@author: Arthur
"""

'''
    Calculate the maximum sum of consecutive elements within an array
    
    e.g. for array [-2, -5, 6, -2, -3, 1, 5, -6] the maximum sum is 7 (6-2-3+1+5, as the numbers must be consecutive)
'''
arr = [-2, -5, 6, -2, -3, 1, 5, -6]

'''
1. 1st naive implementation. What is the complexity?
'''


def max_subarray_sum_very_slow(array: list):
    maximum = array[0]
    for i in range(0, len(array)):
        for j in range(i, len(array)):
            s = 0
            for k in range(i, j + 1):
                s += array[k]
                if s > maximum:
                    maximum = s
    return maximum


'''
2. 2nd naive implementation. What is the complexity?
'''


def max_subarray_sum_slow(array: list):
    maximum = array[0]
    for i in range(0, len(array)):
        s = 0
        for j in range(i, len(array)):
            s += array[j]
            if s > maximum:
                maximum = s
    return maximum


'''
3. Divide & conquer implementation
'''


def max_crossing_sum(array: list, low, middle, high: int):
    """
    Find the maximum possible temp sum in array such that array[middle] is part of it

    input:
        low, high - Low and high bounds, respectively
        middle - the midpoint to consider

    output:
        The value of the maximum crossing temp_sum
    """
    # Include elements on left of middle
    temp_sum = 0
    i = middle
    left_sum = -10 ** 10
    while i >= low:
        temp_sum = temp_sum + array[i]
        i -= 1
        if temp_sum > left_sum:
            left_sum = temp_sum
    # Include elements on right of middle
    temp_sum = 0
    i = middle + 1
    right_sum = -10 ** 10
    while i <= high:
        temp_sum = temp_sum + array[i]
        i += 1
        if temp_sum > right_sum:
            right_sum = temp_sum
    return left_sum + right_sum


def max_subarray_sum(array: list, low, high: int):
    """
    Calculate the maximum subarray sum

    input:
        array - The input array
        low, high - Low and high bounds, respectively

    output:
        The resulting sum value
    """
    if low == high:
        return array[low]

    m = (low + high) // 2
    return max(max_subarray_sum(array, low, m), max_subarray_sum(array, m + 1, high),
               max_crossing_sum(array, low, m, high))


'''
4. Dynamic programming implementation.
'''


def max_subarray(array: list):
    """
    We traverse the array once. For each index i  in the array, we calculate the maximum subarray sum ending at that index.
    If that sum is larger than the one previously recorded, we remember it (in the max_so_far variable)
    """
    max_ending_here = max_so_far = array[0]
    for x in array[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


data = [-2, -5, 6, -2, -3, 1, 5, -6]
print(max_subarray(data))
