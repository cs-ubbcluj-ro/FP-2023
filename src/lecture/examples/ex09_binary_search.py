def binary_search_rec(data: list, key):
    """
    Binary search, recursive implementation
    :param data: List in which search is performed in
    :param key: Search key
    :return: Position of element, -1 if element was not found
    """
    return _binary_search_impl(data, key, 0, len(data) - 1)


def _binary_search_impl(data: list, key, left: int, right: int):
    """
    This is an implementation method. _ means that the method should not be called from other modules.
    """
    if right < left:
        return -1
    m = (left + right) // 2
    if data[m] > key:
        return _binary_search_impl(data, key, left, m - 1)
    if data[m] < key:
        return _binary_search_impl(data, key, m + 1, right)
    if data[m] == key:
        return m


def binary_search_iter(data: list, key):
    left = 0
    right = len(data) - 1

    while left <= right:
        middle = (left + right) // 2
        if data[middle] > key:
            right = middle - 1
        if data[middle] < key:
            left = middle + 1
        if data[middle] == key:
            return middle
    return -1


# TODO Take a look at this method
def test_binary_search():
    binary_search_alg = [binary_search_iter, binary_search_rec]

    for bs_alg in binary_search_alg:
        data = list(range(1000))
        for i in range(0, 1000):
            assert i == bs_alg(data, i)
        assert -1 == bs_alg(list(range(100)), 101)
        assert -1 == bs_alg(list(range(100)), -1)


test_binary_search()
