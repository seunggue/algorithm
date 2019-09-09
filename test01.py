def inorder(n, last):
    global cnt
    if n <= last: # 유효한 노드면
        inorder(n*2, last) # 왼쪽 자식으로 이동
        tree[n] = cnt # visit()
        cnt += 1
        inorder(n*2+1, last)

for t_c in range(int(input())):
    n = int(input())
    tree = [0] * (n+1)
    cnt = 1
    inorder(1,n)
    print('#{} {} {}'.format(t_c+1, tree[1],tree[n//2]))
