"""
Merge Sort implementation
"""


def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]
    merge_sort(left_half)
    merge_sort(right_half)
    merge(left_half, right_half, array)


def merge(l1, l2, lrez):
    i = 0
    j = 0
    l = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l.append(l1[i])
            i = i + 1
        else:
            l.append(l2[j])
            j = j + 1
    while i < len(l1):
        l.append(l1[i])
        i = i + 1
    while j < len(l2):
        l.append(l2[j])
        j = j + 1
    lrez.clear()
    lrez.extend(l)
