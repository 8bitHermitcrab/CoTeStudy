# 시간초과 
import sys
input = sys.stdin.readline
# n, m = map(int, input().split())
n = 4
m = 7

trees = list(map(int, input().split()))

first = max(trees)//2

h, cut = first, 0

while h <= max(trees):
  h, cut = first, 0
  for i in trees:
    if first <= i:
      cut += i-h

  if cut < m:
    first -= 1

  elif cut > m:
    first += 1

  elif cut == m:
    break

print(h)

######################

# 성공

n, m = map(int, input().split())

trees = list(map(int, input().split()))

first, last = 1, max(trees)

while first <= last:
  mid = (first+last) // 2
  cut = 0

  for i in trees:
    if i >= mid:
      cut += i - mid

  if cut < m:
    last = mid - 1
  else:
    first = mid + 1

print(last)