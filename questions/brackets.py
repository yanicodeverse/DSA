def brackets(braketsExp):
    stack = ''
    output = ''

    for braces in braketsExp:
        if (braces == '(') or (braces == '{') or (braces == '['):
            stack += braces
            output += stack

        if (braces == ')'):
            if (stack[-1] == '('):
                stack += braces
                output += stack
        elif (braces == '}'):
            if (stack[-1] == '{'):
                stack += braces
                output += stack
        elif (braces == ']'):
            if (stack[-1] == '['):
                stack += braces
                output += stack

    # while stack:
    #     output += stack
    return output


brackets_ex = '(((())((()))))'
print(brackets(brackets_ex))
