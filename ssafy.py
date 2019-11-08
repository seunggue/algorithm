import sys
sys.stdin = open('input.txt','r')


for t_c in range(int(input())):
    n = int(input())

    food = [list(map(int, input().split())) for _ in range(n)]
    minS = 1000000
    for a_i in range(n):
        for a_j in range(a_i+1,n):
            check = []
            a = food[a_i][a_j] + food[a_j][a_i]
            check.append(a_i)
            check.append(a_j)
            for b_i in range(n):
                for b_j in range(b_i+1,n):

                    if b_i not in check and b_j not in check:
                        b = food[b_i][b_j] + food[b_j][b_i]
                        print(check)
                        print(b_i, b_j)
                        print(a, b)
                        if abs(a-b) < minS:
                            minS = abs(a-b)
    print(minS)

