import sys
sys.stdin = open('input.txt','r')

def num_make(opt_idx, idx, num, opt_list):
    global n, board, opt, max_num, min_num
    print(opt_list)
    print(opt_idx)
    opt_list[opt_idx] += 1

    if opt_list[opt_idx] > opt[opt_idx]:
        return

    if opt_idx == 0:
        num += board[idx+1]
    elif opt_idx == 1:
        num -= board[idx+1]
    elif opt_idx == 2:
        num *= board[idx+1]
    else:
        num = int(num/board[idx+1])

    if idx + 1 == n:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num


    for i in range(4):
        num_make(i,idx+1,num, opt_list[i]+1)



for t_c in range(int(input())):
    n = int(input())
    opt = list(map(int, input().split()))
    board = list(map(int, input().split()))
    opt_list = [0,0,0,0]
    max_num = 0
    min_num = 100000000

    for i in range(4):
        num_make(i,0, board[0], opt_list)


    print(max_num-min_num)



