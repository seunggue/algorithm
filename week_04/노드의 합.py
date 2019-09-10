# import sys
# sys.stdin = open('input.txt','r')

for t_c in range(int(input())):
    n, m, l = map(int, input().split())
    heap = [0] * (n+1)
    for _ in range(m):
        i = list(map(int, input().split()))
        heap[i[0]] = i[1]

    for i in range(n,0,-1):
        heap[i//2] += heap[i]
    print(heap)
    print('#{} {}'.format(t_c+1,heap[m]))