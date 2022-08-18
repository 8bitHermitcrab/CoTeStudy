#https://www.youtube.com/watch?v=CM7RQlYTPcA
from collections import deque

N = int(input())

for _ in range(N):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    #s.sort()
    q = deque()

    for i, x in enumerate(s):
        q.append((i, x))
    
    s.sort()
    cnt = 0
    while q:
        i, x = q.popleft()
        if x == s[-1]:
            s.pop()
            cnt += 1
            if i == m:
                print(cnt)
                break
        else:
            q.append((i, x))

    


    