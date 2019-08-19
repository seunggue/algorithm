for i in range(int(input())):
    def game(page, man):
        start = 1
        score = 0
        end = page
        while start < page:
            center = int((start + end) // 2)
            if center == man:
                return score
            elif center > man:
                score += 1
                end = center
            elif center < man:
                score += 1
                start = center
        return score


    page, a, b = map(int, input().split())
    score_a = game(page,a)
    score_b = game(page,b)
    result = ''
    if score_a > score_b:
        result = 'B'
    elif score_b > score_a:
        result = 'A'
    else:
        result = '0'
    print(f'#{i+1} {result}')