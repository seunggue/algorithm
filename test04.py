# 9.24 최대상금
m,n = map(int, input().split())
m = list(str(m))
start = 0
for i in range(n):
    for s in range(start,len(m)-1):
        print(m[start+s],max(m[start+1:]))
        if m[start+s] < max(m[start+1:]):
            break
        else:
            start += s
    print(start)
    maxM = 0
    for j in range(start+1,len(m)):
        m2 = m[:]
        m2[start],m2[j] = m2[j],m2[start]
        if int(''.join(m2)) > maxM:
            maxM = int(''.join(m2))
    start += 1
    m = list(str(maxM))
    print(m)

print(m)
