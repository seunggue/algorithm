import sys
sys.stdin = open('input2.txt','r')

for t_c in range(int(input())):
    n,m = map(int,input().split())
    contain = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    contain.sort(reverse = True)
    truck.sort(reverse = True)

    result = 0
    cnt = 0
    for i in range(len(contain)):
        for j in range(cnt,len(truck)):
            if contain[i] <= truck[j]:
                result += contain[i]
                cnt += 1
                break
    print('#{} {}'.format(t_c+1,result))
