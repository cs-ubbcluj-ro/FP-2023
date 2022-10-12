import ex01_PrimesLessThan


def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


cache = {0: 0, 1: 1}


def fib_opt(n):
    if n in cache:
        return cache[n]
    cache[n] = fib_opt(n - 2) + fib_opt(n - 1)
    return cache[n]


if __name__ == "__main__":
    print(fib_opt(80))

    # check out these functions
    print(locals())
    print(globals())
