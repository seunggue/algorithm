import sys
sys.stdin = open('input2.txt','r')

for t_c in range(int(input())):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    table.sort(key=lambda x:x[1])

    cnt = 1
    j = 0
    for i in range(len(table)):
        if table[i][0] >= table[j][1]:
            cnt += 1
            j = i
    print('#{} {}'.format(t_c+1,cnt))