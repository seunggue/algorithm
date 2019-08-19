def delete(test):
    test_list = []
    for i in (test):
        if i not in test_list :
            test_list.append(i)
        elif i != test_list[-1]:
            test_list.append(i)
        elif i in test_list and i == test_list[-1]:
            test_list.pop()
    return len(test_list)

for t_c in range(1, int(input())+1):
    test = input()
    print(f'#{t_c} {delete(test)}')