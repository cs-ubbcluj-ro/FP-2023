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

    for i in range(0, len(tokens)):
        tokens[i] = tokens[i].strip()
        tokens[i] = int(tokens[i])

    # check out the eval() function
    result = None
    if symbol == "+":
        result = tokens[0] + tokens[1]
    elif symbol == "-":
        result = tokens[0] - tokens[1]
    elif symbol == "*":
        result = tokens[0] * tokens[1]
    elif symbol == "/":
        result = tokens[0] / tokens[1]

    print("Result: ", result)

print("Goodbye!")
