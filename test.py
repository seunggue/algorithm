import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    arr = [[10*E+1]*(N+1) for _ in range(N+1)]
    #print(arr)
    for i in range(N+1):
        arr[i][i] = 0
    for e in edge:
        r = e[0]
        c = e[1]
        arr[r][c] = e[2]
    print(arr)
    D = arr[0]
    print(D)
    V = set(range(N+1))
    U = {0}
    while U != V:
        B = V - U
        print(B)
        minV = 10*E+1
        for b in B:
            if minV > D[b]:
                minV = D[b]
                minidx = b
        U.add(minidx)
        for w in range(N+1):
            if arr[minidx][w] != 0 and arr[minidx][w] != 10*E+1:
                D[w] = min(D[w], (D[minidx]+arr[minidx][w]))
    print('#{} {}'.format(tc, D[N]))