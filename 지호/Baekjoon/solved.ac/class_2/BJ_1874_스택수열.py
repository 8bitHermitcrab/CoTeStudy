#  백준 1874번 : 스택 수열

import sys
input = sys.stdin.readline

n = int(input())

num = 1
stack = []
c_lst = []

for i in range(n):
  m = int(input())

  while num <= m:
    stack.append(num)
    c_lst.append('+')
    num += 1
  
  if stack[-1] == m:
    stack.pop()
    c_lst.append('-')

  else:
    break

if len(stack) != 0:
  print('NO')
else:
  print(*c_lst, sep='\n')