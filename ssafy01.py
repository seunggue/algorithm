#등산로조성
import sys
sys.stdin = open('input.txt','r')

def find(i,j,cnt,k):
    global n
    global board

    c_i = [0,-1,0,1]
    c_j = [1,0,-1,0]
    for n in range(4):

        n_i = i+c_i[n]
        n_j = j+c_j[n]
        if 0 < n_i < n and 0 < n_j < n:
            if board[i][j] < board[n_i][n_j] and k > 0:
                find(n_i,n_j,cnt+1,0)

            elif


for t_c in range(int(input())):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    top = 0
    for i in range(n):
        if max(board[i]) > top:
            top = max(board[i])
    print(top)
    for i in range(n):
        for j in range(n):
            if board[i][j] == top:
                find(i,j,1,k)
