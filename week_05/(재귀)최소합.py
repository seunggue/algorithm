import sys
sys.stdin = open('input2.txt','r')

def find(i,j,D):
    global minD
    if D > minD:
        return
    if i == n-1 and j == n-1:
        if D < minD:
            minD = D
            return
    if i+1 < n:
        find(i+1,j,D+nxn[i+1][j])
    if j+1 < n:
        find(i,j+1,D+nxn[i][j+1])

for t_c in range(int(input())):
    n = int(input())
    nxn = [list(map(int, input().split())) for _ in range(n)]
    minD = 1000000
    find(0,0,nxn[0][0])
    print('#{} {}'.format(t_c+1,minD))