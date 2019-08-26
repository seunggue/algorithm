for t_c in range(int(input())):
    buses = []
    for n in range(int(input())):
        a,b = map(int, input().split())
        for bus in range(a,b+1):
            buses.append(bus)
    nosun = []
    for p in range(int(input())):
        c = int(input())
        nosun.append(str(buses.count(c)))
    print(f'#{t_c+1} {" ".join(nosun)}')


