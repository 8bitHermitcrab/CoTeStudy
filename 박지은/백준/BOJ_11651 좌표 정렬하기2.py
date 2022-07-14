#220712 화
import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([y,x])

lst2 = sorted(lst)

for j in lst2:
    print(j[1], j[0])