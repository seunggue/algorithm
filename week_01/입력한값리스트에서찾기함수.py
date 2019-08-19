def search(v,arr):
    for check in range(0, len(arr)):
        if arr[check] == v:
            return check + 1
    return '검색실패'

# , 키V
v = int(input())
arr = list(map(int, input().split()))
print(f'{search(v,arr)}번만에 찾음')


