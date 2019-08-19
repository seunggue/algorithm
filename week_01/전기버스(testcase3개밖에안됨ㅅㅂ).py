for t_c in range(int(input())):
    bus = list(map(int, input().split()))
    k = bus[0]
    n = bus[1]
    m = bus[2]
    bus_station = list(map(int, input().split()))
    bus_check = 0
    oil_count = 0
    oil = k + 1
    for i in range(1, n+1):
        next_station = []
        oil -= 1
        if oil_count < k:
            if oil == 0:
                oil_count = 0
                break
            if i in bus_station:
                bus_check += 1
                for next_bus in range(i+1, i+oil):
                    next_station.append(next_bus)
                if bus_check != k:
                    if bus_station[bus_check] in next_station:
                        pass
                    else:
                        oil = k + 1
                        oil_count += 1
                else:
                    oil = k + 1
                    oil_count += 1
    print(f'#{t_c + 1} {oil_count}')


