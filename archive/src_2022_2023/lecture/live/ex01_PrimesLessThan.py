import math

def isPrime(n):
    """
    Verifies if a number is prime.
    :param n: integer
    :return:
        True - if the number n is prime
        False - otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def allPrimesLessThan(n):
    """
    Returns a list with all prime numbers less than a given number n
    :param n: integer
    :return:
    list with prime numbers less than n
    """
    result = []
    for i in range(2, n):
        if isPrime(i):
            result.append(i)
    return result

if __name__ == "__main__":
    while True:
        n = int(input("Input an integer number (0 to exit the program): "))
        if n == 0:
            break
        l = allPrimesLessThan(n)
        print("Prime numbers less than " + str(n) + ": ")
        print(l)