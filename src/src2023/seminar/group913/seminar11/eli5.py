"""
Ways to implement undo/redo
1. Store the repository's state at each operation
    + easy
    - wastes a lot of memory (unless we use state-diffing, kinda like git does)
   Based on the Memento design pattern https://refactoring.guru/design-patterns/memento

2. Store the list of operations the program made
    - harder
    + memory efficient
   Based on the Command design pattern https://refactoring.guru/design-patterns/command

How undo/redo work
    - Undo/redo works globally (no parameters)
    - Redo only works immediately after (at least) an undo
    - Redos are lost when the last operation was not an undo
"""


def fun_function(a, b, c):
    return a + b + c


# remember the call fun_function(3, 5, 8) in order to call it later

fun_name = fun_function
fun_param = (3, 5, 8)
# we call the function now
# () - function call operator
#  * - unpacks the tuple
print(fun_name(*fun_param))
