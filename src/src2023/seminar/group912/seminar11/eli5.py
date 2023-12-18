"""
Ways to implement undo/redo.
    1. Remember the state of the repository at each step and revert to older version when needed
       Variant of the Memento design pattern - https://refactoring.guru/design-patterns/memento
            + easy to implement
            - not efficient with memory
       can be improved by state-diffing

    2. Remember the operation that was carried out and repeat it (redo) or revert it (undo)
        This is the Command design pattern - https://refactoring.guru/design-patterns/command
            + memory-efficient
            - not as easy to implement
"""

"""
TODO
    1. Run undo_hard.py --- it should fail :(
    2. In car_service.py, line 22, add the code required to register car deletion for undo/redo
        (copy/paste/adapt code from client_service.py 
    3. Run undo_hard.py --- it should work :)
"""

def my_function(a, b, c, d, e):
    return a + b * c + d + e


func_name = my_function  # () - function call operator
func_params = 1, 2, 3, 4, 5  # (1,2,3,4,5) - tuple

# ...

print(func_name(*func_params))  # * - unpack the tuple
