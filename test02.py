import sys
sys.stdin = open('input.txt','r')

for t_c in range(int(input())):
    #입력에서 16진수 추출
    n,m = map(int, input().split())
    code = [list(input()) for _ in range(n)]
    total_pw = set()

    for i in range(n):
        sw = 0
        pw = ''
        for j in range(m):
            if code[i][j] != '0' or sw == 1:
                if code[i][j] == '0':
                    if j+1 == m:
                        total_pw.add(pw)
                    elif code[i][j+1] == '0':
                        total_pw.add(pw)
                        sw = 0
                        pw = ''
                    elif code[i][j+1] != '0':
                        pw += code[i][j]
                elif code[i][j+1] != '0'or code[i][j] != '0':
                    pw += code[i][j]
                    sw = 1

    total_pw = list(total_pw)
    print(total_pw)

    #16진수를 2진수로 변환
    n_list = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
              '1101', '1110', '1111']
    pw_list = ['3211','2221','2122','1411','1132','1231','1114','1312','1213','3112']
    for pw in total_pw:
        n2_list = []
        for num in pw:
            if '0' <= num <= '9':
                n = ord(num) - ord('0')
            else:
                n = ord(num) - ord('A') + 10
            n2 = n_list[n]
            n2_list += list(n2)
        #print(n2_list)
        #print(len(n2_list))
        dist = len(n2_list)//56
        start = 0
        end = 0
        for e in range(len(n2_list)-1,-1,-1):
            end = e
            if n2_list[e] == '1':
                start = e + 1 - (56*dist)
                break
        #print(end,start)
        #56의 배수만큼 이진수로 만들기
        n2_result = []
        #print(start)
        for i in range(start,end+1):
            n2_result.append(n2_list[i])
        #print(n2_result)
        #print(len(n2_result))


        total_cnt = 0
        cnt = 0
        cnt_check = ''
        resolve_list = []
        for n2 in range(len(n2_result)):
            #print(n2)
            cnt += 1
            #print(cnt)

            if n2+1 == len(n2_result) or n2_result[n2] != n2_result[n2+1]:
                cnt_check += str(cnt//dist)
                cnt = 0
            #print(cnt_check)
            if len(cnt_check) == 4:
                resolve_list.append(pw_list.index(cnt_check))
                cnt_check = ''
        #print(resolve_list)
        result = sum(resolve_list[0:8:2])*3+sum(resolve_list[1:8:2])
        result_sum = 0
        if result % 10 == 0:
            result_sum += sum(resolve_list)
        else:
            pass
    print('#{} {}'.format(t_c+1,result_sum))



