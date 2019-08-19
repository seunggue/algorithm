arr = [list(map(int, input().split())) for i in range(3)]
print(len(arr))
print(len(arr[0]))
#가로합
for i in range(len(arr)):
    garo_sum= 0
    for j in range(len(arr[i])):
        garo_sum += arr[i][j]
    print(f'{i}줄가로합{garo_sum}')

#세로합
for j in range(len(arr[i])):
    sero_sum = 0
    for i in range(len(arr)):
        sero_sum += arr[i][j]
    print(f'{j}줄세로합{sero_sum}')

