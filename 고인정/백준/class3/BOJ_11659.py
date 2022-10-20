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
    # print(n_list[i-1:j])
    # print(sum(n_list[i-1:j]))
    print(sum_list[j] - sum_list[i-1])
# print(f'n, m = {n}, {m}')
# print(f'n_list = {n_list}')
# print(f'i, j = {i}, {j}')

# https://velog.io/@kimdukbae/BOJ-11659-%EA%B5%AC%EA%B0%84-%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0-4-Python