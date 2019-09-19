#비트 연산자 모든 부분집합 계산
#재형이code
arr = [1, 2, 3, 4]
N = 4
s = []
for i in range(0, 1<<N):
    print(i)
    dummy = []
    for j in range(N):
        print(j)
        if i & (1<<j):
            dummy.append(arr[j])
    # if len(dummy) == 3:
    print(dummy)
    s.append(dummy)
print(s)