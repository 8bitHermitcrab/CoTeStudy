# 나는야 포켓몬 마스터 이다솜

import sys

n, m = map(int, sys.stdin.readline().split())

book = dict()

for i in range(1, n+1):
    temp = sys.stdin.readline().rstrip()
    book[i] = temp
    book[temp] = i

for _ in range(m):
    temp = sys.stdin.readline().rstrip()
    if temp.isdigit():
        print(book[int(temp)])
    else:
        print(book[temp])
