# 그래프의 기본과 탐색 연산(bfs문제)
# 풀지 못함아직
def find(n,m,cnt):
    #print(n,m,cnt)

    global minC
    if n == m:
        if cnt < minC:
            minC = cnt
            return
    if cnt > minC:
        return

    if abs(m-(n*2)) < abs(m-n) and abs(m-(n*2)) > 10:
        find(n * 2, m, cnt + 1)
    else:
    # if abs(m-(n*2)) < abs(m-n):
    #     find(n*2,m,cnt+1)
        if abs(m-(n+1)) < abs(m-n):
            find(n+1,m,cnt+1)
        if abs(m-(n-1)) < abs(m-n):
            find(n-1,m,cnt+1)
        if abs(m-(n-10)) < abs(m-n):
            find(n-10,m,cnt+1)


n,m = map(int, input().split())
minC = 1000000
find(n,m,0)
print(minC)