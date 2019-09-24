import sys
sys.stdin = open('input.txt','r')

def find(i,j,check):
    global room
    global maxC
    global minN
    global N
    global visit
    global cnt

    visit[i][j] = 1

    cnt += 1

    c_i = [0,-1,0,1]
    c_j = [1,0,-1,0]

    check.append(room[i][j])

    for n in range(4):
        n_i = i+c_i[n]
        n_j = j+c_j[n]
        if -1 < n_i < N and -1 < n_j < N and visit[n_i][n_j] == 0 and room[n_i][n_j] - room[i][j] == 1:
            print('11111')
            print(i,j)
            print(n_i,n_j)
            find(n_i,n_j,check)
        elif -1 < n_i < N and -1 < n_j < N and visit[n_i][n_j] == 0 and room[i][j] - room[n_i][n_j] == 1:
            print('222222')
            print(i, j)
            print(n_i, n_j)
            find(n_i,n_j,check)
        else:
            if cnt > maxC and cnt > 1:
                maxC = cnt
                minN = min(check)
            elif cnt == maxC:
                if min(check) < minN:
                    minN = min(check)

for t_c in range(int(input())):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    minN = 10000000
    maxC = 0
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cnt = 0
            check = []
            find(i,j,check)
    print('#{} {} {}'.format(t_c+1,minN, maxC))