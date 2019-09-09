#시간초과남
for t_c in range(int(input())):
    N, M = map(int, input().split())
    n_list = list(input().split())
    for _ in range(M-1):
        n_append = list(input().split())
        for i in range(len(n_list)):
            sw = 0
            if int(n_list[i]) > int(n_append[0]):
                for j in range(len(n_append)):
                    n_list.insert(i+j,n_append[j])
                sw = 1
                break
        if sw == 0:
            for j in n_append:
                n_list.append(j)
    print('#{} {}'.format(t_c+1," ".join(n_list[:-11:-1])))
