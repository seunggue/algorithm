for t_c in range(int(input())):
    n,m,k = map(int, input().split())
    int_list = [list(map(int, input().split())) for _ in range(n)]
    max_int = 0
    for i in range(n-k+1):
        for j in range(m-k+1):
            tedu_sum = 0
            for tedu_i in range(k):
                if tedu_i == 0 or tedu_i == k-1:
                    for tedu_j in range(k):
                        tedu_sum += int_list[tedu_i+i][tedu_j+j]
                else:
                    for tedu_j in range(0,k,k-1):
                        tedu_sum += int_list[tedu_i+i][tedu_j+j]
            if tedu_sum > max_int:
                max_int = tedu_sum
    print(f'#{t_c+1} {max_int}')
