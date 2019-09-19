def x(n,cnt):
    if cnt == m:
        return n
    else:
        return n * x(n,cnt+1)

for t_c in range(10):
    t_c = int(input())
    n,m = map(int, input().split())
    result = 0
    print('#{} {}'.format(t_c, x(n,1)))