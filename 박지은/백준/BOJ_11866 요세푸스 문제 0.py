#220713
#https://hongcoding.tistory.com/41
from collections import deque

queue = deque()
answer = []

n, k = map(int, input().split())

for i in range(1, n+1):
    queue.append(i)

while queue:
    #print('---------------------------')
    #print(queue)
    for i in range(k-1):
        queue.append(queue.popleft())
        #print(queue)
    #print('**********************')
    answer.append(queue.popleft())
    #print(queue)

print("<",end='')
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")