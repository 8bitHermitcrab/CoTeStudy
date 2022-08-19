# BJ 10845번 : 큐

import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
  k = input().split()
  
  if k[0] == 'push':
    stack.append(k[1])
  
  elif k[0] == 'pop':
    if not stack:
      print(-1)
    else: 
      print(stack.pop(0))

  elif k[0] == 'size':
    print(len(stack))

  elif k[0] == 'empty':
    if not stack:
      print(1)
    else:
      print(0)

  elif k[0] == 'front':
    if not stack:
      print(-1)
    else: 
      print(stack[0])

  elif k[0] == 'back':
    if not stack:
      print(-1)
    else: 
      print(stack[-1])