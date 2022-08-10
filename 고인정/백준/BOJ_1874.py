# 스택 수열

n = int(input())

answer = []
stack = []
flag = 0
cnt = 1

for _ in range(n):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        answer.append("+")
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)


# https://hongcoding.tistory.com/39