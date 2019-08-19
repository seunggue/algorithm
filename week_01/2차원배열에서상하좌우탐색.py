arr = [[0]*5 for i in range(5)]
k = 1
for i in range(0,5):
    for j in range(0, 5):
        arr[i][j] = k
        k += 1

#모든 칸의 이웃을 출력
for i in range(0,5):
    for j in range(0,5):
        if j+1 <= 4: # 오른쪽칸이 존재
            print(arr[i][j+1], end=' ')
        if i+1 <= 4: # 아래칸이 존재
            print(arr[i+1][j], end=' ')
        if j-1 >= 0: # 왼쪽칸이 존재
            print(arr[i][j-1], end=' ')
        if i-1 >= 0: # 왼쪽칸이 존재
            print(arr[i-1][j], end=' ')
        print()
    print()

