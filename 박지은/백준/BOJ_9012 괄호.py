#BOJ_4949 균형잡힌 세상 코드 응용

N = int(input())

for _ in range(N):
    
    #문장 입력
    s = input()
    
    #판단하는 임시 리스트(길이가 0이면 YES, 0이 아니면 NO)
    temp = []
    
    for i in s:
        if i == '(':
            temp.append(i)

    
        elif i == ')':
            # ')' 나올 때마다 짝이 맞는 괄호 빼주기
            if len(temp)>0 and temp[-1] == '(':
                temp.pop()
            # 짝이 맞지 않으면 리스트에 ')' 추가
            else:
                temp.append(')')
                break
    
    #짝이 맞는경우
    if len(temp) == 0:
        print('YES')
    #짝이 안맞거나 순서가 안맞을 경우
    else:
        print('NO')