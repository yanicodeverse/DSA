Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

# dictionary having priorities of Operators
Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def infixToPostfix(expression):

    stack = []  # initialization of empty stack

    output = ''

    for character in expression:

        if character not in Operators:  # if an operand append in postfix expression

            output += character

        elif character == '(':  # else Operators push onto stack

            stack.append('(')

        elif character == ')':

            while stack and stack[-1] != '(':

                output += stack.pop()

            stack.pop()

        else:

            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:

                output += stack.pop()

            stack.append(character)

    while stack:

        output += stack.pop()

    return output


if __name__ == '__main__':

    expression = '((A^B*C)^I*(D-Z)/M+N)'

    print('infix notation: ', expression)

    print('postfix notation: ', infixToPostfix(expression))
