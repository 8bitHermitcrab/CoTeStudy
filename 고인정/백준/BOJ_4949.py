# 균형잡힌 세상

while True:
    words = input()
    stack = []

    # 마침표로 멈춤
    if words == '.':
        break
    
    for word in words:
        if word == '[' or word == '(':
            stack.append(word)

        # 대괄호
        elif word == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        # 소괄호
        elif word == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    
    if len(stack) == 0:
        print('yes')
    else:
        print('no')


# print(string)

# https://velog.io/@pmk4236/%EB%B0%B1%EC%A4%80-4949%EB%B2%88-%EA%B7%A0%ED%98%95%EC%9E%A1%ED%9E%8C-%EC%84%B8%EC%83%81-Python