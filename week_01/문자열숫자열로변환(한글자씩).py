def atoi(s):
    n = 0
    for i in range(0, len(s)):
        n = n * 10
        n = n + int(s[i])
    return n

s = input()
r = atoi(s)
print(r)