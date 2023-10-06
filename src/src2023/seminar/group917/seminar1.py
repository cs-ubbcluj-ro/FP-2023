def compute(a: int, b: int, symbol: str) -> float:
    if symbol == '+':
        return a + b
    elif symbol == '-':
        return a - b
    elif symbol == '*':
        return a * b
    elif symbol == '/':
        return a / b


# TO DO (modifications): add validation function
# renaming (optional)
#
print("This is a calculator app. Available operations: +, -, *, /. exit to stop.")
operations = '+-/*'
while True:
    cmd = input(">>>")
    op_count = 0
    # for index in range(len(operations)):
    for op in operations:
        op_count += cmd.count(op)

    if op_count != 1:
        print("Invalid command. Please try again.")
        continue
    if cmd.lower().strip() == 'exit':
        break
    else:
        userlist = cmd.split()
        if len(userlist) != 3:
            print("Please enter a valid command.")
            continue

        a = int(userlist[0])
        b = int(userlist[2])
        result = compute(a, b, userlist[1])
        print('Result is:', result)
# if 'exit' in cmd.lower():
#     break
