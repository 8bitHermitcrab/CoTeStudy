# 괄호 회전하기

# s = "[](){}"
# s = "[)(]"
s = "}]()[{"
# s = "}}}}"

def solution(s):
    answer = 0
    s_list = list(s)
    # print(s_list)

    for _ in range(len(s)):
        stack = []
        for i in range(len(s)):
            print(f's_list = {s_list}')
            print(f'i = {i} // stack = {stack}')
            if len(stack) > 0:
                if stack[-1] == '(' and s_list[i] == ')':
                    stack.pop()
                elif stack[-1] == '[' and s_list[i] == ']':
                    stack.pop()
                elif stack[-1] == '{' and s_list[i] == '}':
                    stack.pop()
                else:
                    stack.append(s_list[i])
            else:
                stack.append(s_list[i])
        if len(stack) == 0:
            answer += 1
        s_list.append(s_list.pop(0))
    return answer

print(solution(s)) 

# https://foameraserblue.tistory.com/87

'''
# 괄호 돌려보기
def rotation_s(s):
    s = s[1:] + s[0]
    return s

# print(f'rotation_s(s) = {rotation_s(s)}')

# 괄호가 올바른지 체크
def checking_bracket(s):
    result = False
            
    stack = []
    if len(s) % 2 == 1:
        result = False
    else:
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            if s[i] == '[': 
                stack.append(s[i])
            if s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if '(' in stack:
                    stack.remove('(')
                    # print(f'stack = {stack}')
            if s[i] == ']':
                if '[' in stack:
                    stack.remove('[')
                    # print(f'stack = {stack}')
            if s[i] == '}':
                if '{' in stack:
                    stack.remove('{')
                    # print(f'stack = {stack}')

        print(f'stack = {stack}')

        if len(stack) != 0:
            result = False
            # print(f'F_stack = {stack}')
        else:
            result = True
            # print(f'T_stack = {stack}')
    
    rs = s
    rs_list = []
    rs_list.append("a"*len(s))
    rs_list.append("b"*len(s))
    rs_list.append("c"*len(s))
    rs_list.append("d"*len(s))
    rs_list.append("e"*len(s))
    rs_list.append("f"*len(s))
    # print(f'rs_list = {rs_list}')
    
    rs = rs.replace("(", "a")
    rs = rs.replace(")", "b")
    rs = rs.replace("[", "c")
    rs = rs.replace("]", "d")
    rs = rs.replace("{", "e")
    rs = rs.replace("}", "f")
    # print(f'rs = {rs}')

    if rs in rs_list:
        result = False

    return result

# print(f'checking_bracket(s) = {checking_bracket(s)}')

def solution(s):
    answer = 0
    
    # 각 괄호의 앞부분이 나온 개수만큼 올바름?
    # '(', ')', '[', ']', '{', '}'
    
    # s[::-1]
    # print(f's[::-1] = {s[::-1]}')
    
    for _ in range(len(s)):
        # print(f's = {s}')
        if checking_bracket(s) == True:
            answer += 1
        s = rotation_s(s)
        # print(f'rs = {s}')

    
    return answer

print(solution(s))

# 괄호 첫 부분이 홀수 자리에 있을 때
        # if i % 2 == 1:
        #     if 
'''


'''
stack = []

    if len(s) % 2 == 1:
        answer = 0
    else:
        for i in range(len(s)):
            # if s[i] == '(' or '[' or '{':
            if s[i] == '(':
                stack.append(s[i])
            if s[i] == '[': 
                stack.append(s[i])
            if s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if '(' in stack:
                    answer += 1
                    stack.remove('(')
                    print(f'stack = {stack}')
            if s[i] == ']':
                if '[' in stack:
                    answer += 1
                    stack.remove('[')
                    print(f'stack = {stack}')
            if s[i] == '}':
                if '{' in stack:
                    answer += 1
                    stack.remove('{')
                    print(f'stack = {stack}')

    print(f'stack = {stack}')

    if len(stack) != 0:
        answer = 0
'''