# 지뢰찾기
import sys
sys.stdin = open('input2.txt','r')

def find(i,j,sw):
    global board,n,cnt,c_i,c_j

    # if sw == 1:
    #     mine = 0
    #     for c in range(8):
    #         n_i = i + c_i[c]
    #         n_j = j + c_j[c]
    #         if 0 <= n_i < n and 0 <= n_j < n:
    #             if board[n_i][n_j] == '*':
    #                 mine = 1
    #                 break
    #     if mine == 0:
    #         for c in range(8):
    #             n_i = i + c_i[c]
    #             n_j = j + c_j[c]
    #             if 0 <= n_i < n and 0 <= n_j < n:
    #                 board[n_i][n_j] = '1'
    #         if i+1 < n:
    #             find(i+1,j,1)
    #         if j+1 < n:
    #             find(i,j+1,1)
    #
    # elif sw == 0:
    #     for c in range(8):
    #         n_i = i + c_i[c]
    #         n_j = j + c_j[c]
    #         if 0 <= n_i < n and 0 <= n_j < n:
    #             board[n_i][n_j] = '1'
    #     if i + 1 < n:
    #         find(i + 1, j, 1)
    #     if j + 1 < n:
    #         find(i, j + 1, 1)



for t_c in range(int(input())):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    cnt = 0
    c_i = [0,-1,-1,-1,0,1,1,1]
    c_j = [1,1,0,-1,-1,-1,0,1]

    for i in range(n):
        for j in range(n):

            if board[i][j] == '.':

                mine = 0
                for c in range(8):
                        n_i = i+c_i[c]
                        n_j = j+c_j[c]
                        if 0 <= n_i < n and 0 <= n_j < n:
                            if board[n_i][n_j] == '*':
                                mine = 1
                                break

                if mine == 0:
                    cnt += 1
                    board[i][j] = '1'
                    find(i,j,0)

    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                cnt += 1
    print(cnt)