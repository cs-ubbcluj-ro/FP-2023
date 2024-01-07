"""
Ways to implement undo/redo
1. Deep copy the entire list of objects and restore them on undo
    + easy to implement
    - inefficient use of memory
   Based on the Memento design pattern https://refactoring.guru/design-patterns/memento
    can be improved using state-diffing

2. Remember the action, its parameters and reverse it for undo
    + efficient use of memory
    - harder to implement
    Based on the Command design pattern https://refactoring.guru/design-patterns/command

What to do
    0. git update FP repository
    1. run undo_hard.py (client is restored instead of the car)
    2. in car_service.py, line 22 add support for undoing car
        deletion (it's in client_service.py lines 27 - 29)
    3. check that undo_hard.py works correctly

"""


def fun_fun_fun(a, b, c, d, e):
    return a + b + c * d + e


fun_name = fun_fun_fun
fun_params = 1, 2, 3, 4, 5
# ...
print(fun_name(*fun_params))
