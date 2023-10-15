def fact(n: int) -> int:
    # 1. Base case, n == 0
    if n == 0:
        return 1
    # 2. Make the recursion progress towards the base case
    return n * fact(n - 1)


def fact_opt(accumulator: int, n: int) -> int:
    # 1. Base case, n == 0
    if n == 0:
        return accumulator
    # 2. Make the recursion progress towards the base case
    return fact_opt(n * accumulator, n - 1)


print(fact_opt(1, 4))


# print(fact(5000))


def fib(n: int) -> int:
    """
    Calculate the n-th term of the Fibonacci sequence
    :param n: the index of the term
    :return: The term's value
    """
    # 1. Base case, we break recursion
    if n < 2:
        return n
    # 2. Progress towards the base case
    return fib(n - 2) + fib(n - 1)


# print(fib(10))

def fib_iter(n: int) -> int:
    x = 0
    y = 1
    for i in range(n):
        z = x + y
        x = y
        y = z
    return x


def test_fib():
    for i in range(10):
        # assert is used for unit testing
        # AssertionError if the condition is not True
        # last parameter gets printed out to help debug the issue
        assert fib(i) == fib_iter(i), (i, fib(i), fib_iter(i))


test_fib()


"""
    n -> size of the program's input
    T(n) -> function that describes how many operations are made for input size n
    O(n) -> function that provides a high bound on complexity
    Omega(n) -> low bound
    Theta(n) -> O(n) AND Omega(n)
    
    
    bubble-sort, worst case
    T(n) = (n - 1) + (n - 2) + ... + 1 => T(n) in O(n^2)
    
    fib iterative
    T(n) = 1 + n, T(n) in O(n)
    
    fib recursive 
    T(n) = 1 + T(n-2) + T(n-1)
"""
