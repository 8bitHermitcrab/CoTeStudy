# Four Squares

# n - (n보다 작거나 같은 제곱수) 를 인덱스로 갖는 값에 +1

# pypy3에서만 정답 처리됨.
# python3에서는 시간 초과 처리됨.

import sys

INPUT = sys.stdin.readline

n = int(INPUT())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    j = 1
    min_sn = 4
    # min_sn = 1e9
    while (j**2) <= i :
        # temp = n_list[i-(j**2)]
        min_sn = min(min_sn, dp[i-(j**2)])
        j += 1
    dp[i] = min_sn + 1

print(dp[n])

# https://imzzan.tistory.com/79

# https://jeongm1n.tistory.com/entry/%EB%B0%B1%EC%A4%80-DP17626-Four-Squares-Python

'''
n = int(input())
n_list = [0, 1]

for i in range(2, n+1):
    j = 1
    min_sn = 4
    while (j**2) <= i :
        temp = n_list[i-(j**2)]
        min_sn = min(min_sn, temp)
        j += 1
    n_list.append(min_sn + 1)

print(n_list[n])
'''