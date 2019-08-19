#n = int(input())
box = list(map(int, input().split()))
if sum(box) % len(box) == 0:
    count = 0
    print('0나옴')
    while (max(box)-min(box)) != 0:
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1
        count += 1
    print(count)
else:
    print('0안됨')
    count = 0
    while (max(box)-min(box)) != 1:
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1
        count += 1
    print(count)


