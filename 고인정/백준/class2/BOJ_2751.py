# 수 정렬하기 2

import sys

n = int(sys.stdin.readline())

num = [int(sys.stdin.readline()) for _ in range(n)]

# 오름차순 정렬
num.sort()

for i in num:
    print(i)