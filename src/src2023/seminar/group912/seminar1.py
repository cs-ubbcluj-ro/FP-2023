# print("Hello World!")

"""
Write a calculator program that supports the +, -, *, / for integers. Exit the program by typing "exit"
"""

# s = input("Enter a string >")

"""
    1. The type of 1024 becomes the type of var s
    2. The value of 1024 becomes the value of s 
"""

print("Welcome to calculator. Print exit to quit.")
# command = input(">>>")

command = '   123 +      45   '
command = command.strip()
tokens = command.split("+")

print(tokens)
for i in range(0, len(tokens)):
    tokens[i] = tokens[i].strip()

print(tokens)
