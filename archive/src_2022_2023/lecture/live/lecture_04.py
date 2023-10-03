"""
Return the product of the positive numbers found on even positions in a list, or None if there are no positive numbers
on an even position.
"""


def array_product_iter(array: list):
    max_len = 0
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
            max_len = max(max_len, len(stack))
            print(stack)

    return product, max_len


data = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
print(array_product_iter(data))
