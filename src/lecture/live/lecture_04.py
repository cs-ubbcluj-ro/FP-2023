"""
Return the product of the positive numbers found on even positions in a list, or None if there are no positive numbers
on an even position.
"""


def array_product_iter(array: list):
    product = 1

    stack = [(0, len(array) - 1)]

    while len(stack) > 0:
        left, right = stack.pop()

        if left == right:
            if left % 2 == 0 and array[left] > 0:
                product *= array[left]
        else:
            mid = (left + right) // 2
            stack.append((left, mid))
            stack.append((mid + 1, right))

    return product


data = [1, 2, 5, 2, 2, 2, 6, 7, 8, 2, 11, 9, 4, 5]
print(array_product_iter(data))
