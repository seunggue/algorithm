import sys
sys.setrecursionlimit(10000)

def game(s_i,s_j):

    global ladder2
    c_i = [0,0,1]
    c_j = [1,-1,0]
    if ladder2[s_i][s_j] == 2:
        print(f'찾음{s_j}')
        return 'find'
    else:
        ladder2[s_i][s_j] = 0
    for k in range(3):
        i = s_i + c_i[k]
        j = s_j + c_j[k]
        if j < 10 and j > -1 and i < 10 and ladder2[i][j] >0:
            print(f'{i} {j}로 이동')
            game(i,j)




for _ in range(1):
    n = int(input())
    ladder = [list(map(int,input().split())) for _ in range(10)]
    for j in range(10):
        ladder2 = ladder[:]
        if ladder[0][j] == 1:
            print(f'{j}로 이동!!!!')
            if game(0,j) == 'find':
                print(f'#{n} {j}')
                break



