s = []
choice = 0
c = 'y'
while c == 'y':
    print('\n1. PUSH ')
    print('2. POP')
    print('3. DISPLAY')
    choice = int(input('Enter your choice= '))
    if choice == 1:
        a = input('Enter a number: ')
        s.append(a)
    elif choice == 2:
        if s == []:
            print('Stack is Empty')
        else:
            print('Deleted item is ', s.pop())
    elif choice == 3:
        l = len(s)
        print("Stack is: ")
        for i in range(l - 1, -1, -1):
            print(s[i], end=' ')
    else:
        print('Wrong input')
    c = input('\nEnter your choice y/n: ')
