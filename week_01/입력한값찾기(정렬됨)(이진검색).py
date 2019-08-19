def search(key,arr):
    left = 0
    right = len(arr) - 1
    while (left <= right):
        center = (left + right) // 2
        if key == arr[center]:
            return 1
        elif arr[center] < key:
            # 작은구간 버림
            left = center + 1
        elif key < arr[center]:
            # 큰구간 버림
            right = center - 1

# , 키V
key = int(input())
arr = list(map(int, input().split()))
print(f'{search(key,arr)}번만에 찾음')




