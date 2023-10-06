def compute(a: int, b: int, symbol: str) -> float:
    if symbol == '+':
        return a + b
    elif symbol == '-':
        return a - b
    elif symbol == '*':
        return a * b
    elif symbol == '/':
        return a / b


# TO DO (modifications): add validation function/move validation in function

print("This is a calculator app. Available operations: +, -, *, /. Type exit to stop.")
operations = '+-/*'

while True:
    cmd = input(">>>")
    cmd = cmd.lower().strip()
    operator_count = 0

    if cmd == 'exit':
        break

    for operator in operations:
        operator_count += cmd.count(operator)

    if operator_count != 1:
        print("Invalid command. Please try again.")
        continue

    tokens = cmd.split()

    # Do we still need this check after adding the verification above?
    # What do we check here? Can we provide more information to the user about why
    # their command was not valid?
    if len(tokens) != 3:
        print("Invalid command. Please try again.")
        continue

    left_operand = int(tokens[0])
    right_operand = int(tokens[2])
    result = compute(left_operand, right_operand, tokens[1])
    print('Result is:', result)
