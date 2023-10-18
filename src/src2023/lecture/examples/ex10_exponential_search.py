from ex09_binary_search import binary_search_impl


def exponential_search(data: list, key):
    if len(data) == 0 or data[0] > key or data[-1] < key:
        return -1

    if data[0] == key:
        return 0

    i = 1
    while i < len(data) and data[i] <= key:
        i = i * 2

    return binary_search_impl(data, key, i // 2, min(i, len(data) - 1))
