for test_case in range(1,int(input())+1):
    paper = [[0,0,0,0,0,0,0,0,0,0] for i in range(10)]
    for i in range(int(input())):
        box = list(map(int, input().split()))
        start_i = box[0]
        start_j = box[1]
        garo = box[2]-box[0]+1
        sero = box[3]-box[1]+1
        color = box[4]
        for i in range(start_i,start_i+garo):
            for j in range(start_j, start_j+sero):
                paper[i][j] += color
    bora_count = 0
    for i in range(10):
        bora_count += paper[i].count(3)
    print(f'#{test_case} {bora_count}')