#https://blog.naver.com/dngmlwo336/222660304285

# 시작하는 괄호를 리스트에 저장하면서 바로 직전에 짝이 
# 맞는 친구들이 나오면 pop()일 이용해서 괄호 제거하기

# 리스트에 아무것도 없으면 짝이 맞은것, 아니면 짝이 맞지 않은 것

while True:
    s = input()

    # .만 입력하면 while문 빠져나오기
    if s == '.':
        break

    temp = []

    for i in s:
        if i == '[' or i == '(':
            temp.append(i)
        elif i == ']':
            if len(temp)>0 and temp[-1] == '[':     #len(temp)>0 안붙이면 에러나옴
                temp.pop()
            else:
                temp.append(']')
                break
        elif i == ')':
            if len(temp)>0 and temp[-1] == '(':
                temp.pop()
            else:
                temp.append(')')
                break
    
    #짝이 맞는경우
    if len(temp) == 0:
        print('yes')
    #짝이 안맞거나 순서가 안맞을 경우
    else:
        print('no')
