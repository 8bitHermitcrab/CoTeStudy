#백준 9012번 문제 코드 그대로...

def solution(s):
    
    #체크용 임시 리스트
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
    
    #길이로 판단(길이가 0이면 true, 0이 아니면 false)
    #짝이 맞는 경우
    if len(temp) == 0:
        answer = True
    #짝이 안맞거나 순서가 안맞을 경우
    else:
        answer = False
    return answer