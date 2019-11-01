#재귀 호출을 통한 순열 생성
# def perm2(n,k,m):
#     if n == k:
#         print(p[:3])
#     else:
#         for i in range(n,m):
#             p[n], p[i] = p[i], p[n]
#             perm2(n+1, k, m)
#             p[n], p[i] = p[i], p[n]
# p = [1,2,3,4,5]
# perm2(0,3,5)
# print('=========================================')
def perm(n,k):
    #print(s)
    if n == k:
        print('=============')
        print(s)
    else:
        for i in range(n,k):
            s[n], s[i] = s[i], s[n]
            perm(n+1, k)
            s[n], s[i] = s[i], s[n]
s = [1,2,3,4,5]
perm(0,5)


