def find(j,check,p):
    global minP
    if p > minP:
        return

    if len(check) == n:
        if p < minP:
            minP = p
    for i2 in range(n):
        if i2 not in check:
            find(j+1,check+[i2],p+f[i2][j+1])

for t_c in range(int(input())):
    n = int(input())
    f = [list(map(int, input().split())) for _ in range(n)]
    minP = 2000
    for i in range(n):
        check = []
        find(0,check+[i],f[i][0])
    print('#{} {}'.format(t_c+1,minP))