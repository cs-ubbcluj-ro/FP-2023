"""
Created on Nov 1, 2016

@author: Arthur
"""


class FirstClass:
    pass


class SecondClass:
    def __init__(self):
        self.test_one = "Test One"
        self._test_two = "Test Two"
        self.__test_three = "Test Three"


x = FirstClass()

'''
    What is the type of x ?
'''
print(type(x))

'''
    An empty class, such as FirstClass can be used as a Pascal record or a C struct
'''
x.name = "Alice"
x.salary = 100
x.salary += 20
print("Name of x=", x.name)
print("Salary of x=", x.salary)

y = FirstClass()
y.name = "Bob"
y.salary = 1000
print("Name of y=", y.name)
print("Salary of y=", y.salary)

'''
What happens if we add another field on-the-fly?
'''
y.hello = "Say hello"
print(y.hello)
# Field 'hello' is not a part of instance 'x'
# print(x.hello)

'''
How about the more complex, SecondClass example?
'''
obj = SecondClass()
print(obj.test_one)
# print(obj._test_two)

'''
This is Python's name mangling at work
'''
# print(obj.__test_three)
# print(obj._SecondClass__test_three)
