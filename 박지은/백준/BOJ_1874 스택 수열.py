#https://blog.naver.com/hanjo1515/222499722591
#문제를 이해 못하겠어요ㅜ

n = int(input())

stack = []
result = []
nums = [x+1 for x in range(n)]
answer = []

#입력
for _ in range(n):
    result.append(int(input()))


i = 0
cnt = 0
while(True):
    #빈 stack에 추가하기
    #push
    if stack == []:
        stack.append(nums[i])
        answer.append('+')
        i += 1
    else:
        #pop
        if stack[len(stack)-1] == result[cnt]:
            stack.pop()
            answer.append('-')
            cnt += 1
        else:
            if i == n:
                print('NO')
                break
            stack.append(nums[i])
            answer.append('+')
            i += 1
    #출력
    if cnt == n:
        print(*answer, sep = '\n')
        break