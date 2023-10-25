"""
Created on Jan 11, 2017

@author: Arthur
"""
import math

''' 
Function to get minimum number of trails needed in worst # case with n eggs and k floors

input:
    n - Number of eggs remaining
    k - Number of floors

output:
    The number of minimum drops, if following optimal solution
    
    credit - This code is contributed by Bhavya Jain
    http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/
'''


def egg_drop(n, k):
    """
    A 2D table where every egg_floor[i][j] will represent minimum
    number of trials needed for i eggs and j floors.
    """
    egg_floor = [[0 for x in range(k + 1)] for x in range(n + 1)]

    '''
    We need one trial for one floor and0 trials for 0 floors
    '''
    for i in range(1, n + 1):
        egg_floor[i][1] = 1
        egg_floor[i][0] = 0

    '''
    We always need j trials for one egg and j floors.
    '''
    for j in range(1, k + 1):
        egg_floor[1][j] = j

    '''
    Fill rest of the entries in table using optimal substructure property
    '''
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            egg_floor[i][j] = math.inf
            for x in range(1, j + 1):
                res = 1 + max(egg_floor[i - 1][x - 1], egg_floor[i][j - x])
                if res < egg_floor[i][j]:
                    egg_floor[i][j] = res

    '''
    eggFloor[n][k] holds the result
    '''
    return egg_floor[n][k]


def test_egg_drop():
    n = 2
    k = 100
    print("Minimum number of drops in the worst case with " + str(n) + " eggs and " + str(k) + " floors is " + str(
        egg_drop(n, k)))


test_egg_drop()
