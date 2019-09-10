import sys
sys.stdin = open('input.txt','r')

def check(buho,left,right):
    #global result
    left = int(left)
    right = int(right)
    check = ['+','-','/','*']
    print(buho,left,right)
    if n_list[left-1][1] in check:
        print(left,type(n_list[left-1][1]))
        n_list[left-1][1] = check(n_list[left - 1][1],n_list[left - 1][2],n_list[left - 1][3])
    elif n_list[right-1][1] in check:
        print(right,type(n_list[right - 1][1]))
        n_list[right-1][1] = check(n_list[right - 1][1], n_list[right - 1][2], n_list[right - 1][3])


    if buho == '-':
        return n_list[left-1][1] - n_list[right-1][1]
    elif buho == '+':
        return n_list[left-1][1] + n_list[right-1][1]
    elif buho == '/':
        return n_list[left-1][1] / n_list[right-1][1]
    elif buho == '*':
        return n_list[left-1][1] * n_list[right-1][1]

n = int(input())
n_list = [list(input().split()) for _ in range(n)]
result = 0
result = check(n_list[0][1],n_list[0][2],n_list[0][3])
print(int(result))
