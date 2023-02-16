from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
p = list(map(int, input().split()))
deq = deque([i for i in range(1, N+1)])

count = 0

for i in p:
  while True:
    if deq[0] == i:
      deq.popleft()
      break
        
    else:
      if deq.index(i) <= len(deq)//2:
        while deq[0] != i:
          deq.rotate(-1)
          count += 1
      
      else:
        while deq[0] != i:
          deq.rotate(1)
          count += 1

print(count)