# 앞뒤 글자 바꾸기
s = list(input())

for i in range(0, len(s)//2):
    s[i],s[len(s)-1-i] = s[len(s)-1-i], s[i]

for i in range(0, len(s)):
    print(s[i], end='')
print('조인을 쓰면')
print(''.join(s))

