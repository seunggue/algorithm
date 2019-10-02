for t_c in range(int(input())):
    m,d = map(int, input().split())
    num = 0
    for i in range(1,m):
        if i in [1,3,5,7,8,10,12]:
            num += 31
        elif i in [4,6,9,11]:
            num += 30
        elif i == 2:
            num += 29
    num += d
    num = num % 7 + 3
    if num >= 7:
        num -= 7
    print('#{} {}'.format(t_c+1,num))