def callPoints(ops):
    stack = []
    for i in ops:
        if i == '+':
            stack.append(stack[-1] + stack[-2])
        elif i == 'D':
            stack.append(stack[-1]*2)
        elif i == 'C':
            if stack == []:
                print('Stack is Empty')
            else:
                stack.pop()
        else:
            stack.append(int(i))

    return sum(stack)


ops = ["23", "D", "+", "2", "1"]
print(callPoints(ops))
