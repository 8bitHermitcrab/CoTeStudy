# 백준 1654번 : 랜선 자르기

import sys
input = sys.stdin.readline

k, n = map(int, input().split())

len = [int(input()) for _ in range(k)]

short_len, long_len = 1, max(len)

while short_len <= long_len:
  mid_len = (short_len + long_len) // 2
  count_line = 0
  for i in len:
    count_line += i//mid_len
  
  if count_line >= n:
    short_len = mid_len + 1
    answer = mid_len
  else:
    long_len = mid_len -1

print(answer)