def preorder(idx,e,find):
    if idx > 0:
        if tree[idx] == find:
            preorder(ch1[n])
            preorder(ch2[n])
        preorder(ch1[n])
        preorder(ch2[n])



e,n = map(int,input().split())
tree = list(map(int, input().split()))

ch1 = [0] * e+1
ch2 = [0] * e+1

for i in range(e-1):
    p = tree[2*i]
    c = tree[2*i+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

preorder(1,e,find)