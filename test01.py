# 인수의 생일 파티
import sys
sys.stdin = open('input.txt','r')


def find2()

def find(i,j,cnt,check,start,end,sw):
    global maxC
    global minC
    global minC2
    print('====={}====='.format(sw))
    print(i,j,cnt)
    if j == end and sw == 1:
        print('집도착')
        if cnt > minC:
            return
        else:
            minC = cnt
            check = []
            find(j,j,0,check,end,start,2)
            return

    elif j == end and sw == 2:
        print('여기옴????')
        if cnt < minC2:
            minC2 = cnt
            if minC + minC2 > maxC:
                print('maxC가즈아')
                print(minC,minC2)
                maxC = minC+minC2
                print(maxC)
                return

    check.append(i)

    for tree in trees:
        if tree[1] not in check and tree[0] == j:
            find(tree[0],tree[1],cnt+tree[2],check,start,end,sw)

N,M,X = map(int,input().split())
trees = [list(map(int, input().split())) for _ in range(M)]
maxC = 0
for tree in trees:
    cnt = 0
    check = []
    minC = 100000000
    minC2 = 100000000
    find(tree[0],tree[1],cnt+tree[2],check,tree[0],X,1)
print(maxC)