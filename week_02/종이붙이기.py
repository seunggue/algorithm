def paper(n):
    if n ==1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n-1) + paper(n-2) *2

for i in range(int(input())):
    n = int(input()) // 10
    print(f'#{i+1} {paper(n)}')