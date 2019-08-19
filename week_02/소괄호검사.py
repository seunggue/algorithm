# 소괄호 검사
# 괄호의 짝이 맞으면 1 아니면 0리턴
def f(txt):
    s = list() # 스택생성
    for i in range(len(txt)):
        if(txt[i]=='('): # 여는 괄호면 push()
            s.append(txt[i])
        elif(txt[i]==')'): # 닫는 괄호면 pop()해서 비교
            if(len(s)==0): # 스택이 비어있다면 오류
                return 0
            else: # 스택이 비어있지 않다면 여는 괄호 하나 꺼냄
                s.pop()

    if(len(s)!=0):
        return 0
    else:
        return 1


t = int(input())
for tc in range(1, t+1):
    txt = input()
    print(f(txt))