"""
Add the code below to https://pythontutor.com/visualize.html
Check the evolution of the call stack step by step
"""


def fib(n: int):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


print(fib(8))
