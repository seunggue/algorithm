def preorder(idx):
    global cnt

    if idx > 0:
        cnt += 1
        preorder(ch1[idx])
        preorder(ch2[idx])

for t_c in range(int(input())):
    e,n = map(int,input().split())
    tree = list(map(int, input().split()))

    ch1 = [0] * (e+2)
    ch2 = [0] * (e+2)
    cnt = 0

    for i in range(e):
        p = tree[2*i]
        c = tree[2*i+1]

        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    preorder(n)
    print('#{} {}'.format(t_c+1, cnt))