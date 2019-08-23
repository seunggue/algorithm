#섬사이즈 없이 카운트만
def land(i, j):
    global n
    global sea
    c_i = [0, -1, -1, -1, 0, 1, 1, 1]
    c_j = [1, 1, 0, -1, -1, -1, 0, 1]
    sea[i][j] = 0
    for c in range(8):
        if j + c_j[c] < n and i + c_i[c] > 0 and j + c_j[c] > 0 and i + c_i[c] < n and sea[i + c_i[c]][j + c_j[c]] > 0:
            land(i + c_i[c], j + c_j[c])
    return

for t_c in range(int(input())):
    n = int(input())
    sea = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for sea_i in range(n):
        for sea_j in range(n):
            if sea[sea_i][sea_j] > 0:
                cnt += 1
                land(sea_i,sea_j)
    print(f'#{t_c+1} {cnt}')