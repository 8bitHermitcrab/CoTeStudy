# 좌표 정렬하기 2

# import sys

n = int(input())
# n = int(sys.stdin.readline())

xy = []

for _ in range(n):
    (x, y) = input().split()
    # (x, y) = sys.stdin.readline().split()
    xy.append((int(x), int(y)))

# xy = sorted(xy, key=lambda y:y[1])
# xy = sorted(xy, key=lambda x:x[0])
xy = sorted(xy, key=lambda x:(x[1], x[0]))
# print(xy)

for i in xy:
    print(i[0], i[1])

# https://pdache.github.io/python/boj/BOJ-11651/