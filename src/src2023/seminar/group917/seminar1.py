print("This is a calculator app. Available operations: +, -, *, /. exit to stop.")
userlist = []
while True:
    cmd = input(">>>")
    print(cmd)

    if cmd.lower().strip() == 'exit':
        break
    else:

        userlist = cmd.split()
        a = int(userlist[0])
        b = int(userlist[2])
        if userlist[1] == '+':
            print(a+b)
        elif userlist[1] == '-':
            print(a-b)
        elif userlist[1] == '*':
            print(a*b)
        elif userlist[1] == '/':
            print(a/b)

# if 'exit' in cmd.lower():
#     break
