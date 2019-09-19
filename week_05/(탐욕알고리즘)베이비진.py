import sys
sys.stdin = open('input2.txt','r')

def game(card):
    p1 = []
    p2 = []
    for i in range(0,len(card),2):
        p1.append(card[i])
        p2.append(card[i+1])
        p1.sort()
        p2.sort()
        p1_run,p1_tri,p2_run,p2_tri,result = 0,0,0,0,0
        for j in range(0,len(p1)):
            if j == 0:
                continue

            if p1[j] == p1[j-1]:
                p1_tri += 1
            else:
                p1_tri = 0
            if p1[j]-1 == p1[j-1]:
                p1_run += 1
            elif p1[j] == p1[j-1]:
                pass
            else:
                p1_run = 0

            if p2[j] == p2[j-1]:
                p2_tri += 1
            else:
                p2_tri = 0
            if p2[j]-1 == p2[j-1]:
                p2_run += 1
            elif p2[j] == p2[j-1]:
                pass
            else:
                p2_run = 0

            if p1_run == 2 or p1_tri == 2:
                result += 1
            if p2_run == 2 or p2_tri == 2:
                result += 2

            if result > 0:
                if result == 3:
                    result = 0
                    return result
                else:
                    return result
    return result

for t_c in range(int(input())):
    card = list(map(int, input().split()))

    print('#{} {}'.format(t_c+1,game(card)))


