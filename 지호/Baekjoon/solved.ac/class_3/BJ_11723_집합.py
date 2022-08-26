# 백준 11723번 : 집합

import sys
input = sys.stdin.readline

s = set()
m = int(input())

for _ in range(m):
  x = input().split()

  if len(x) == 1:
    if x[0] == 'all':
      s = set(range(1, 21))
    else:
      s = set()

  else:
    p, q = x[0], int(x[1])

    if p == 'add':
      if q not in s:
        s.add(q)
    
    elif p == 'remove':
      if q in s:
        s.discard(q)

    elif x[0] == 'check':
      if x[1] in s:
        print(1)
      else:
        print(0)

    elif x[0] == 'toggle':
      if x[1] in s:
        s.discard(x[1])
      else:
        s.add(x[1])