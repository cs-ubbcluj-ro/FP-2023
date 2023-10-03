# print("Hello World!")

"""
Write a calculator program that supports the +, -, *, / for natural numbers. Exit the program by typing "exit"
"""

# s = input("Enter a string >")

"""
    1. The type of 1024 becomes the type of var s
    2. The value of 1024 becomes the value of s 

    <number> <op> <number>
    <op> is one of +, -, *, /
"""


def calculate(x: int, y: int, symbol: str) -> float:
    # check out the eval() function
    if symbol == "+":
        return x + y
    elif symbol == "-":
        return x - y
    elif symbol == "*":
        return x * y
    elif symbol == "/":
        return x / y
    else:
        raise ValueError("Unknown operation")


operations = "+-*/"
print("Welcome to calculator. Print exit to quit.")

while True:
    command = input(">>>")
    command = command.strip()

    if command == "exit":
        break

    index = 0
    symbol = ''

    for oper in operations:
        index += command.count(oper)
        if index == 1 and symbol == '':
            symbol = oper

    if index != 1:
        print("Invalid expression")
        break

    tokens = command.split(symbol)
    oper_left = int(tokens[0].strip())
    oper_right = int(tokens[1].strip())

    print("Result: ", calculate(oper_left, oper_right, symbol))

print("Goodbye!")
