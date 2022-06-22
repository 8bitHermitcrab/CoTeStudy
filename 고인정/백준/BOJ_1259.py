# 팰린드롬수

while True:
    n = int(input())
    if n != 0:
        str_n = str(n)
        # print(f'str_n = {str_n}')
        reverse_n = str_n[-1::-1]
        # print(f'reverse_n = {reverse_n}')
        if n == int(reverse_n):
            print('yes')
        else:
            print('no')
    else:
        break