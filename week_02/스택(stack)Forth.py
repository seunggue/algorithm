def forth(calc):
    stack = []
    result = 0
    for cal in calc:

        if cal != '+'and cal != '-'and cal != '*' and cal != '/' and cal != '.':
            stack.append(cal)
        elif cal == '+' and len(stack) >= 2:
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a+b)
        elif cal == '-' and len(stack) >= 2:
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a-b)
        elif cal == '*' and len(stack) >= 2:
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a*b)
        elif cal == '/' and len(stack) >= 2:
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a//b)
        elif cal == '.' and len(stack) == 1:
            return stack.pop()
        else:
            return 'error'
    return 'error'

for t_c in range(int(input())):
    calc = list(input().split())
    print(f'#{t_c + 1} {forth(calc)}')