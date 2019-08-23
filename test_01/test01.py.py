for t_c in range(int(input())):
    n , m = map(int, input().split())
    emp_list = [[0]*n for _ in range(n)]
    for _ in range(m):
        left_i, left_j, right_i, right_j = map(int, input().split())
        for i in range(left_i-1, left_i+(right_i-left_i)):
            for j in range(left_j-1, left_j+right_j-left_j):
                emp_list[i][j] = 1

    cnt = 0
    for emp in emp_list:
        cnt += emp.count(1)
    print(f'#{t_c+1} {cnt}')
