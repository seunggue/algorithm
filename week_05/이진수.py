for t_c in range(int(input())):
    n, n_16 = input().split()
    n = int(n)
    n_list = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    result = ''
    for i in range(n):
        if '0' <= n_16[i] <= '9':
            digit = ord(n_16[i]) - ord('0')
        else:
            digit = ord(n_16[i]) - ord('A') + 10
        result += n_list[digit]
    print('#{} {}'.format(t_c+1,result))