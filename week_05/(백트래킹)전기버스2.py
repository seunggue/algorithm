def find(hold,m,N,c):
    global minC
    if c > minC:
        return

    for i in range(m):
        if hold+i+1 < N-1:
            find(hold+i+1,M[hold+i+1],N,c+1)
        elif hold+i+1 == N-1:
            if c < minC:
                minC = c

for t_c in range(int(input())):
    a = list(map(int, input().split()))
    N,M = a[0],a[1:]
    M.append(0)
    minC = 100
    find(0,M[0],N,0)
    print('#{} {}'.format(t_c+1,minC))