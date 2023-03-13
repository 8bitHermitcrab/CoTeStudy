import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_lst = []

for _ in range(N):
    n_lst.append(input())

count = 0

for i in range(M):
    x = input()
    if x in n_lst:
        count += 1

print(count)
