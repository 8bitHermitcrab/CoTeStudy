# 큐

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import collections

n = int(input())

order = []
que = collections.deque()

for _ in range(n):
    order.append(input().split())

for i in range(n):
    if order[i][0] == 'push':
        que.append(order[i][1])
    elif order[i][0] == 'pop':
        if len(que) != 0:
            print(que.popleft())
        else:
            print(-1)
    elif order[i][0] == 'size':
        print(len(que))
    elif order[i][0] == 'empty':
        if len(que) != 0:
            print(0)
        else:
            print(1)
    elif order[i][0] == 'front':
        if len(que) != 0:
            print(que[0])
        else:
            print(-1)
    elif order[i][0] == 'back':
        if len(que) != 0:
            print(que[-1])
        else:
            print(-1)


# https://excelsior-cjh.tistory.com/96