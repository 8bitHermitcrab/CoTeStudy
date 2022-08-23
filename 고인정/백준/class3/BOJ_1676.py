# 팩토리얼 0의 개수

import math

n = int(input())
num = math.factorial(n)
# print(f'num = {num}')
cnt = 0

str_num = str(num)
# print(str_num)
len_num = len(str_num)
# print(f'len_num = {len_num}')

for i in range(len_num-1, 0, -1):
    # print(f'i = {i}')
    # print(f'str_num[{i}] = {str_num[i]}')
    if str_num[i] == '0':
        cnt += 1
        # print(f'cnt = {cnt}')
    else:
        break

print(cnt)
