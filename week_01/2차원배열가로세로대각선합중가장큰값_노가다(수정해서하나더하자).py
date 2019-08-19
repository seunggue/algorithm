for test_case in range(10):
    n = int(input())
    num_list = [list(map(int, input().split())) for i in range(100)]
    max = 0
    for i in range(100):
        num_sum = 0
        for j in range(100):
            num_sum += num_list[i][j]
        if num_sum > max:
            max = num_sum

    for j in range(100):
        num_sum = 0
        for i in range(100):
            num_sum += num_list[i][j]
        if num_sum > max:
            max = num_sum

    num_sum = 0
    for e in range(100):
        num_sum += num_list[e][e]
    if num_sum > max:
        max = num_sum

    num_sum = 0
    for f in range(100):
        num_sum += num_list[f][99-f]
    if num_sum > max:
        max = num_sum
    print(f'#{n} {max}')