def bracket(test):
    bracket_list = []
    for i in test:
        if i == '(' or i == '{':
            bracket_list.append(i)
        elif i == ')' or i == '}':
            if i == ')':
                a = '('
            elif i == '}':
                a = '{'
            if len(bracket_list) == 0 or bracket_list[-1] != a:
                return 0
            else:
                bracket_list.pop()

    if bracket_list == []:
        return 1
    else:
        return 0


for i in range(1, int(input())+1):
    test = input()
    print(f'#{i} {bracket(test)}')