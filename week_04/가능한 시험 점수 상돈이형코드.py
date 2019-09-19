#상돈이형 가능한 시험 점수 코드
n = int(input())
arr = list(map(int,input().split()))
check = [0]*(sum(arr) + 1)
subSet = [0]
check[0] = 1
for num in arr:
    temp = list(subSet)
    for i in temp:
        if not check[i + num]:
            check[i + num] = 1
            subSet += [i + num]

print(sum(check))