# 좌표 정렬하기

import sys

n = int(sys.stdin.readline())

xy = []

for _ in range(n):
    (x, y) = sys.stdin.readline().split()
    xy.append((int(x), int(y)))

xy.sort()

for i in xy:
    print(i[0], i[1])

# https://wook-2124.tistory.com/464