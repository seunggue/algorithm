for t_c in range(int(input())):
    n = float(input())
    s = 1
    cnt = 0
    result = ''
    while n != 0:
        cnt += 1
        s /= 2
        if n >= s:
            n -= s
            result += '1'
        else:
            result += '0'
        if cnt == 13:
            result = 'overflow'
            break
    print('#{} {}'.format(t_c+1,result))
