# 올바른 괄호

# s = "()()"
# s = "(())()"
# s = ")()("
s = "(()("

def solution(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()

    return stack == []


print(solution(s))


# https://velog.io/@ssongplay/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%98%AC%EB%B0%94%EB%A5%B8-%EA%B4%84%ED%98%B8-Python

'''
def solution(s):
    stack = []

    if s[0] == ')':
        answer = False
    else:
        for i in s:
            if i == '(':
                stack.append(i)
                # print(f'1stack = {stack}')
            elif i == ')':
                if len(stack) > 0:
                    if stack[-1] == '(':
                        stack.pop()
                        if len(stack) == 0:
                            answer = True
                        else:
                            answer = False
                else:
                    answer = False

    return answer'''