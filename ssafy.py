import sys
sys.stdin = open('input.txt','r')

def num_make(op_idx, idx, num):
    global board, opt_list, max_num, min_num, op

    opt_list[i] += 1
    if op_idx == 0:
        num += board[idx]
    elif op_idx == 1:
        num -= board[idx]
    elif op_idx == 2:
        num *= board[idx]
    else:
        num = int(num / board[idx])

    if opt_list[op_idx] > op[op_idx]:
        return


for t_c in range(int(input())):
    n = int(input())
    op = list(map(int, input().split()))
    board = list(map(int, input().split()))
    opt_list = [0,0,0,0]
    max_num = 0
    min_num = 100000000
    for i in range(4):
        num_make(i,0, board[0])
    print(max_num-min_num)



