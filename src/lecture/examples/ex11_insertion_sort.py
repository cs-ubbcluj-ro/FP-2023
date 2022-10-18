"""
Insertion sort. An O(n^2) complexity algorithm
"""


def insertion_sort(data: list):
    for i in range(1, len(data)):
        val = data[i]
        j = i - 1
        while (j >= 0) and (data[j] > val):
            data[j + 1] = data[j]
            j = j - 1
            data[j + 1] = val
    return data


"""
Binary insertion sort
Source: https://www.geeksforgeeks.org/binary-insertion-sort/ (code contributed by Mohit Gupta_OMG)
"""


def binary_search(arr, val, start, end):
    # we need to distinguish whether we should insert before or after the left boundary. imagine [0] is the last
    # step of the binary search and we need to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    # this occurs if we are moving beyond left's boundary meaning the left boundary is the least position to find a
    # number greater than val
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def binary_insertion_sort(data: list):
    for i in range(1, len(data)):
        val = data[i]
        j = binary_search(data, val, 0, i - 1)
        # This is O(n) space complexity, but it can be simplified by moving elements one by one
        data = data[:j] + [val] + data[j:i] + data[i + 1:]
    return data
