import sys
sys.stdin = open('input.txt','r')

def find(i,j,t_num,time):
    global cnt,N,M,board
    c_i = [0,-1,0,1]
    c_j = [1,0,-1,0]
    cnt += 1
    if time == 0:
        return

    for c in range(4):
        n_i = i + c_i[c]
        n_j = j + c_j[c]
        n_t = board[n_i][n_j]
        if 0 <= n_i < N and 0 <= n_j < M:
            if (c == 0 or c == 1) and (n_t == 3 or n_t == 6 or n_t == 7):
                find(n_i,n_j,n_t,time-1)
            elif (c == 2 or c == 3) and (n_t == 2 or n_t == 4 or n_t == 5):
                find(n_i,n_j,n_t,time-1)






for t_c in range(int(input())):
    N,M,R,C,L = map(int(input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    find(R,C,board[R][C],L-1)