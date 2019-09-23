import sys
sys.stdin = open('input.txt','r')

# KRUSKAL알고리즘 최소신장트리
def rep(n):
    print('======================')
    print(p)
    print(n)
    print('======================')
    while p[n] != n:
        n = p[n]

    return n

for t_c in range(int(input())):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge.sort(key=lambda x:x[2]) #가중치를 기준으로 오름차순 정렬
    p = [i for i in range(V+1)] #대표원소 배열
    print(p)
    cnt = 0
    s = 0
    for x in edge: #N개의 노드(V+1)가 있는 경우 N-1개의 간선을 선택(V)
        print(x)
        n0 = rep(x[0])
        n1 = rep(x[1])
        print(n0,n1)
        if n0 != n1: #두 노드의 대표 원소가 다르면 mst에 추가
            p[n1] = n0
            cnt += 1 #간선을 선택한 경우
            s += x[2] #가중치의 합
            if cnt == V:
                break
    print('#{} {}'.format(t_c+1,s))
