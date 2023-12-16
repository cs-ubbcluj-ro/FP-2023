def g(a, b, c):
    sum_abc = a + b + c
    return sum_abc


def f(a, *args):
    print(a)
    print(*args)  # this is a tuple
    print(g(*args))


#f(1)
#f(1, 2, 3, 4, 5, 6, 7)
# f(10, [4, 5, 6], 9)
f(1, 2, 3, 4)

print('----'*10)


def sum_of_squares(lst):
    s = 0
    for el in lst:
        s += pow(el, 2)
    return s

def sum_simple(lst):
    return sum(lst)

def function_with_fn_as_param(lst, sum_fn):
    return sum_fn(lst)

test_list = [1,2,3,4]
print('Simple sum - just add elements')
# sum_simple = 333
print(function_with_fn_as_param(test_list,sum_simple))
print('Sum of squares')
print(function_with_fn_as_param(test_list,sum_of_squares))
