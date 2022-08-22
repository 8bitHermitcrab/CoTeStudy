# 수 정렬하기3

# 수 정렬하기 3

import sys

n = int(sys.stdin.readline())

check_list = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    check_list[num] = check_list[num] + 1

print(f'check_list = {check_list}')

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)