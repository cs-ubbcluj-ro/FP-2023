from random import randint


def binary_search(data: list, key: int) -> int:
    # recursive version
    # T(n) = T(n/2) + 1, n > 1
    return binary_search_impl(data, key, 0, len(data) - 1)


def binary_search_impl(data: list, key: int, left: int, right: int) -> int:
    # if right > len(data) -1

    if left > right:
        return -1

    if left == right:
        if data[left] == key:
            return left
        return -1

    m = (left + right) // 2

    if data[m] < key:
        # print(m, right)
        return binary_search_impl(data, key, m + 1, right)
    elif data[m] > key:
        # print(left, m)
        return binary_search_impl(data, key, left, m - 1)
    else:
        return m


def test_search():
    # test functions don't have input parameters and don't return values

    data = list(range(0, randint(0, 1000)))
    # data = list(range(0, 10))
    # -1 should not be in the list
    assert binary_search(data, -1) == -1
    # 1001 should not be in the list
    assert binary_search(data, 1001) == -1, len(data)

    # check each element is in place
    for i in range(0, len(data)):
        assert i == binary_search(data, data[i])


# check that Python script was started from this module
if __name__ == "__main__":
    test_search()
