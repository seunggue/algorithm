for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    min_n, max_n = 0, 0
    for c in range(0, n-m+1):
        num = 0
        for c2 in range(c,c+m):
            num += nums[c2]
        if min_n == 0:
            min_n = num
        if num <= min_n:
            min_n = num
        if num >= max_n:
            max_n = num
    print(f'#{i} {max_n-min_n}')
