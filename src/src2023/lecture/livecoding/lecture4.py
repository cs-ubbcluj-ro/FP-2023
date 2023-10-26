"""
Return the product of the positive numbers found on even positions in a list,
knowing the list has at least one such number.
"""


def list_product(data: list) -> int:
    """
    Return the product of the positive numbers found on even positions in a list,
knowing the list has at least one such number.
    :param data: The list
    :return: Calculated product
    """
    pass


def list_product_chip_conquer(data: list) -> int:
    if len(data) < 3:
        return data[0] if data[0] > 0 else 1
        # C# --> ?:
    return (data[0] if data[0] > 0 else 1) * list_product_chip_conquer(data[2:])


def test_list_product_chip_conquer():
    assert list_product_chip_conquer([1, 2, 3, 4]) == 3
    assert list_product_chip_conquer([4]) == 4
    assert list_product_chip_conquer([4, 2, -3, 4]) == 4
    assert list_product_chip_conquer([2, 2]) == 2
    assert list_product_chip_conquer([1, 2, 3, 4, 5, 1, 2]) == 30
    assert list_product_chip_conquer([-1, 2, 3, 4, -5, 1, -2]) == 3


def test_list_product_rec():
    assert list_product_rec([1, 2, 3, 4]) == 3
    assert list_product_rec([4]) == 4
    assert list_product_rec([4, 2, -3, 4]) == 4
    assert list_product_rec([2, 2]) == 2
    assert list_product_rec([1, 2, 3, 4, 5, 1, 2]) == 30
    assert list_product_rec([-1, 2, 3, 4, -5, 1, -2]) == 3


def _list_product_rec(data: list, left: int, right: int) -> int:
    if left == right:
        #     if left % 2 == 0 and data[left] > 0:
        #         return data[left]
        #     else:
        #         return 1
        # <=>
        return data[left] if left % 2 == 0 and data[left] > 0 else 1

    m = (left + right) // 2
    return _list_product_rec(data, left, m) * _list_product_rec(data, m + 1, right)


def list_product_rec(data: list) -> int:
    return _list_product_rec(data, 0, len(data) - 1)


def test_list_product_iter():
    assert list_product_iter([1, 2, 3, 4]) == 3
    assert list_product_iter([4]) == 4
    assert list_product_iter([4, 2, -3, 4]) == 4
    assert list_product_iter([2, 2]) == 2
    assert list_product_iter([1, 2, 3, 4, 5, 1, 2]) == 30
    assert list_product_iter([-1, 2, 3, 4, -5, 1, -2]) == 3


def list_product_iter(data: list) -> int:
    stack = []
    product = 1

    stack.append((0, len(data) - 1))
    while len(stack) > 0:
        left, right = stack.pop()

        if left == right:
            product *= data[left] if left % 2 == 0 and data[left] > 0 else 1
        else:
            m = (left + right) // 2
            stack.append((left, m))
            stack.append((m + 1, right))
    return product


test_list_product_chip_conquer()
test_list_product_rec()
test_list_product_iter()
