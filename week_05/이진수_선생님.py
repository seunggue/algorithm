n, n_16 = input().split()

n = int(n)
for i in range(n):
    if '0' <= n_16[i] <= '9':
        digit = ord(n_16[i]) - ord('0')
    else:
        digit = ord(n_16[i]) - ord('A') + 10

    for j in range(3,-1,-1):
        if digit & (1 << j) == 0:
            print('0',end='')
        else:
            print('1', end='')
        print()