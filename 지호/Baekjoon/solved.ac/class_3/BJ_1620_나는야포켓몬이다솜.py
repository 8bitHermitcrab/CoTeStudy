# 백준 1620번 : 나는야 포켓몬 마스터 이다솜

# 320ms

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = dict()

lst = []

for i in range(n+m):
  dic = input().rstrip()
  if i < n:
    d[str(i+1)] = dic
  else:
    lst.append(dic)

d_reversed = {v:k for k,v in d.items()}

for i in lst:
  if i in d.keys():
    print(d[i])
  else:
    print(int(d_reversed[i]))


# 256ms

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = dict()

lst = []

for i in range(n):
  dic = input().rstrip()
  d[dic] = i+1
  lst.append(dic)

for i in range(m):
  test = input().rstrip()
  if test.isdigit():
    print(lst[int(test)-1])
  else:
    print(d[test])