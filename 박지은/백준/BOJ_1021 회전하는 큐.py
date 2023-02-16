#from collections import deque

n, m = map(int, input().split())
data = list(map(int, input().split()))
d = deque(i+1 for i in range(n))
answer = 0

for i in data:
    if d[0] != i:
        if d.index(i) < len(d) - d.index(i):
            while True:
                d.append(d.popleft()) #두 번째 연산
                answer += 1
                if d[0] == i:
                    d.popleft()
                    break

        else:
            while True:
                d.appendleft(d.pop()) #세 번째 연산
                answer += 1
                if d[0] == i:
                    d.popleft()
                    break
    else:
        d.popleft()


print(answer)
from collections import deque

n, m = map(int, input().split())
data = list(map(int, input().split()))
d = deque(i+1 for i in range(n))
answer = 0

for i in data:
    if d[0] != i:
        if d.index(i) < len(d) - d.index(i):
            while True:
                d.append(d.popleft()) #두 번째 연산
                answer += 1
                if d[0] == i:
                    d.popleft()
                    break

        else:
            while True:
                d.appendleft(d.pop()) #세 번째 연산
                answer += 1
                if d[0] == i:
                    d.popleft()
                    break
    else:
        d.popleft()


print(answer)