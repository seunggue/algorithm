import sys
sys.stdin = open('input2.txt','r')

def perm(n,k):
    global s
    global result
    global minD
    if n == k:
        s += [1]
        D = 0
        for i in range(n):
            D += nxn[s[i]-1][s[i+1]-1]
            if D > minD:
                break
        if D < minD:
            minD = D
    else:
        for i in range(n,k):
            s[n], s[i] = s[i], s[n]
            perm(n+1, k)
            s[n], s[i] = s[i], s[n]

for t_c in range(int(input())):
    n = int(input())
    nxn = [list(map(int, input().split())) for _ in range(n)]
    s = []
    minD = 100000000
    for i in range(1,n+1):
        s.append(i)
    perm(1,n)
    print('#{} {}'.format(t_c+1,minD))
