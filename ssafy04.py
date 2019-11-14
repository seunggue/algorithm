import sys
sys.stdin = open('input.txt','r')

def find(i,j,t_num,time):
    global cnt,N,M,board,visit
    c_i = [0,-1,0,1]
    c_j = [1,0,-1,0]
    cnt += 1
    visit[i][j] = 1
    if time == 0:
        return

    t_meet = []

    if t_num == 1:
        t_meet = [0,1,2,3]
    elif t_num == 2:
        t_meet = [1,3]
    elif t_num == 3:
        t_meet = [0,2]
    elif t_num == 4:
        t_meet = [0,1]
    elif t_num == 5:
        t_meet = [0,3]
    elif t_num == 6:
        t_meet = [2,3]
    elif t_num == 7:
        t_meet = [1,2]

    for c in t_meet:
        n_i = i + c_i[c]
        n_j = j + c_j[c]
        if 0 <= n_i < N and 0 <= n_j < M and visit[n_i][n_j] == 0:
            n_t = board[n_i][n_j]

            if c == 0:
                if n_t == 1 or n_t == 3 or n_t == 6 or n_t == 7:
                    find(n_i,n_j,n_t,time-1) 
            elif c == 1:
                if n_t == 1 or n_t == 2 or n_t == 5 or n_t == 6:
                    find(n_i,n_j,n_t,time-1)
            elif c == 2:
                if n_t == 1 or n_t == 3 or n_t == 4 or n_t == 5:
                    find(n_i,n_j,n_t,time-1)
            elif c == 3:
                if n_t == 1 or n_t == 2 or n_t == 4 or n_t == 7:
                    find(n_i,n_j,n_t,time-1)


for t_c in range(int(input())):
    N,M,R,C,L = map(int,input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]


    cnt = 0
    find(R,C,board[R][C],L-1)
    for v in visit:
        print(v)
    print(cnt)