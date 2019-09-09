for t_c in range(int(input())):
    n, m ,l = map(int, input().split())
    n_list = list(map(int, input().split()))
    for _ in range(m):
        idx, num = map(int, input().split())
        n_list.insert(idx, num)
    print('#{} {}'.format(t_c+1, n_list[l]))