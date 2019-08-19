#텍스트 파일자동으로 인풋해주는
import sys
sys.stdin = open('input.txt','r')

t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    print(arr)