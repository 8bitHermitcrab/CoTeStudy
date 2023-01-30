t = int(input())

for _ in range(t):
  count = 0
  
  x1, y1, x2, y2 = map(int, input().split())
  
  n = int(input())

  for _ in range(n):
    cx, cy, r = map(int, input().split())
    dist1 = ((x1-cx)**2 + (y1-cy)**2)**0.5
    dist2 = ((x2-cx)**2 + (y2-cy)**2)**0.5

    if r > dist1 and r > dist2:
      pass
    elif r > dist1 or r > dist2:
      count += 1
  
  print(count)