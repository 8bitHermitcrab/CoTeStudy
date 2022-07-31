import sys
input = sys.stdin.readline

N = int(input())

stackk = []

for _ in range(N):
    #print(stackk)
    #입력
    x = input().split()
    #print(x)

    #push X: 정수 X를 스택에 넣는 연산
    if x[0] == 'push':
        stackk.append(x[1])

    #pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력. 스택에 들어있는 정수가 없는 경우에는 -1을 출력
    elif x[0] == 'pop':
        if stackk == []:
            print(-1)
        else:
            p = stackk.pop()
            print(p)

    #size: 스택에 들어있는 정수의 개수를 출력
    elif x[0] == 'size':
        print(len(stackk))

    #empty: 스택이 비어있으면 1, 아니면 0을 출력
    elif x[0] == 'empty':
        if stackk == []:
            print(1)
        else:
            print(0)

    #top: 스택의 가장 위에 있는 정수를 출력. 스택에 들어있는 정수가 없는 경우에는 -1을 출력.
    elif x[0] == 'top':
        if stackk == []:
            print(-1)
        else:
            print(stackk[-1])

