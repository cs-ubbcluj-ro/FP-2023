import math
import random


def generate_list(n: int) -> list:
    """
    Generate a list of length n filled with pseudo random integers
    :param n: the number of integers to put in the list
    :type n: int
    :return: list of numbers
    :rtype: list
    """
    return [random.randint(-n, n) for i in range(n)]


"""
Time complexity? 
O(n^3)
"""


# Naive implementation: generate all subsets and compute sum for each
def max_sum_naive(array: list) -> (int, int, int):
    """
    Compute maximum subarray sum and start&end indices for corresponding subarray
    :param array: list in which we search the subset
    :type array: list
    :return: maximum sum, and the start and end indices for the subarray, in this order
    :rtype: tuple - (int, int, int)
    """
    max_subarray_sum = -math.inf
    subarray_end = -1
    subarray_begin = -1

    for i in range(len(array)):
        for j in range(i + 1, len(array) + 1):
            current_subset = array[i:j]
            # also count sum() complexity
            # at each step len(current_subset) -> Complexity of max_sum_naive: Theta(n^3)
            current_sum = sum(current_subset)

            print('Current subset is:', current_subset, 'with sum', current_sum)

            if current_sum > max_subarray_sum:
                max_subarray_sum = current_sum
                subarray_end = j
                subarray_begin = i

    return max_subarray_sum, subarray_begin, subarray_end


"""
Complexity: O(n^2)
"""


def max_subarray_sum_naive2(arr: list):
    if len(arr) == 0:
        return 0
    max_sum = arr[0]
    for i in range(len(arr)):
        crt_sum = 0
        for j in range(i, len(arr)):
            crt_sum += arr[j]
            if crt_sum > max_sum:
                max_sum = crt_sum

    return max_sum


"""
Time complexity?
T(n) = 2T(n/2) + n
     = ...
     O(nlogn)
"""


# Divide and conquer implementation: divide in halves + take 'crossing' arrays
def max_sum_dc(array: list, left: int, right: int):
    if left == right:
        return array[left]

    middle = (left + right) // 2
    left_sum = max_sum_dc(array, left, middle)
    right_sum = max_sum_dc(array, middle + 1, right)

    left_sum_crossing = 0
    max_left_crossing = -math.inf
    for i in range(middle, left - 1, -1):
        left_sum_crossing += array[i]
        if left_sum_crossing > max_left_crossing:
            max_left_crossing = left_sum_crossing

    right_sum_crossing = 0
    max_right_crossing = -math.inf
    for i in range(middle + 1, right + 1):
        right_sum_crossing += array[i]
        if right_sum_crossing > max_right_crossing:
            max_right_crossing = right_sum_crossing

    max_crossing_sum = max_left_crossing + max_right_crossing
    return max(left_sum, right_sum, max_crossing_sum)


"""
Time complexity?
T(n) = n
"""


def max_sum_dp(arr):
    max_sum = -math.inf
    dp = [0] * len(arr)
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])
        max_sum = max(dp[i], max_sum)

    return max_sum


lst = generate_list(10)
print('List is:', lst)
max_sum, max_sum_begin, max_sum_end = max_sum_naive(lst)
print('Subarray with max sum is', lst[max_sum_begin:max_sum_end], 'with sum', max_sum)
res_max_sum_dc = max_sum_dc(lst, 0, len(lst) - 1)
print('Max subarray sum with D&C is', res_max_sum_dc)

res_max_sum_dp = max_sum_dp(lst)
print('Max subarray sum with DP is', res_max_sum_dp)

assert (max_sum == res_max_sum_dc == res_max_sum_dp)
