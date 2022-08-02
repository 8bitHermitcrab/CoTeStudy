import sys
input = sys.stdin.readline

N = int(input())

q = []

for _ in range(N):
    #print(q)
    #입력
    x = input().split()
    #print(x)

    #push X: 정수 X를 큐에 넣는 연산
    if x[0] == 'push':
        q.append(x[1])

    #pop: 큐에서 가장 위에 있는 정수를 빼고, 그 수를 출력. 큐에 들어있는 정수가 없는 경우에는 -1을 출력
    elif x[0] == 'pop':
        if q == []:
            print(-1)
        else:
            p = q[0]
            print(p)
            q.remove(p)

    #size: 큐에 들어있는 정수의 개수를 출력
    elif x[0] == 'size':
        print(len(q))

    #empty: 큐 비어있으면 1, 아니면 0을 출력
    elif x[0] == 'empty':
        if q == []:
            print(1)
        else:
            print(0)

    #front: 큐의 가장 앞에 있는 정수를 출력. 큐에 들어있는 정수가 없는 경우에는 -1을 출력.
    elif x[0] == 'front':
        if q == []:
            print(-1)
        else:
            print(q[0])
    
    #back: 큐의 가장 뒤에 있는 정수를 출력. 큐에 들어있는 정수가 없는 경우 -1을 출력
    elif x[0] == 'back':
        if q == []:
            print(-1)
        else:
            print(q[-1])