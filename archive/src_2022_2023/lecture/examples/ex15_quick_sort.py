"""
QuickSort example
Source code from https://www.geeksforgeeks.org/iterative-quick-sort/ (code is contributed by Mohit Kumra)
"""


def partition(array: list, low: int, high: int):
    i = (low - 1)
    x = array[high]

    for j in range(low, high):
        if array[j] <= x:
            # increment index of smaller element
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


# Function to do Quick sort
# arr[] --> Array to be sorted,
# l --> Starting index,
# h --> Ending index
def quick_sort_but_slow(array: list):
    # Create an auxiliary stack
    low = 0
    high = len(array) - 1
    size = high - low + 1
    stack = [0] * size

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    # Keep popping from stack while is not empty
    while top >= 0:
        # Pop h and l
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(array, low, high)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high


"""
Iterative implementation of quick_sort
Source code from https://stackoverflow.com/questions/66546476/non-recursive-quicksort
User https://stackoverflow.com/users/3282056/rcgldr
"""


def quick_sort(array):
    if len(array) < 2:  # if nothing to sort, return
        return
    stack = [[0, len(array) - 1]]  # initialize stack
    while len(stack) > 0:  # loop till stack empty
        lo, hi = stack.pop()  # pop lo, hi indexes
        p = array[(lo + hi) // 2]  # pivot, any a[] except a[hi]
        i = lo - 1  # Hoare partition
        j = hi + 1
        while 1:
            while 1:  # while(a[++i] < p)
                i += 1
                if array[i] >= p:
                    break
            while 1:  # while(a[--j] < p)
                j -= 1
                if array[j] <= p:
                    break
            if i >= j:  # if indexes met or crossed, break
                break
            array[i], array[j] = array[j], array[i]  # else swap elements
        if j > lo:  # push indexes onto stack
            stack.append([lo, j])
        j += 1
        if hi > j:
            stack.append([j, hi])
