# D3 3282. 0/1 Knapsack
# 백트래킹으로는 나오는데 타임에러 뜸 DP를 써야한다는데 모르겠다시바

import sys
sys.stdin = open('input.txt','r')

def find(i,V,C,check):
    global item
    global maxC
    global K
    #print(i)
    if check == 0:
        pass
    elif V > K:
        return
    elif C > maxC:
        maxC = C

    if i+1 < N:
        find(i+1,V+item[i+1][0],C+item[i+1][1],1)
        find(i+1,V,C,0)

for t_c in range(int(input())):
    N,K = map(int, input().split())
    item = [list(map(int, input().split())) for _ in range(N)]
    item.sort(key=lambda X:X[0])
    print(item)
    maxC = 0
    for i in range(N):
        find(i,item[i][0],item[i][1],1)
    print('#{} {}'.format(t_c+1,maxC))