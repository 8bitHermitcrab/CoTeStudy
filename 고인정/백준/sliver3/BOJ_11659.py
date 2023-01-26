# 구간 합 구하기 4

import sys

INPUT = sys.stdin.readline

n, m = map(int, INPUT().split())
n_list = list(map(int, INPUT().split()))

sum_list = [0]
sum = 0

for i in range(len(n_list)):
    sum += n_list[i]
    sum_list.append(sum)

for _ in range(m):
    i, j = map(int, INPUT().split())
    print(sum_list[j] - sum_list[i-1])