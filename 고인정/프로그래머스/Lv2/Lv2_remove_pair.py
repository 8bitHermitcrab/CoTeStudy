# 짝지어 제거하기

# 1
# s = 'baabaa'
# 0
s = 'cdcd'

def solution(s):
    stack = []
    for i in s:
        print(f'i = {i}')
        if len(stack) == 0:
            stack.append(i)
            print(f'stack = {stack}')

        elif stack[-1] == i:
            stack.pop()
            print(f'stack = {stack}')

        else:
            stack.append(i)
            print(f'stack = {stack}')

    if len(stack) == 0:
        return 1
    else:
        return 0

print(solution(s))

# https://eda-ai-lab.tistory.com/492

'''
def solution(s):
    answer = 0

    alpha = 'abcdefghijklnmopqrstuvwxyz'
    pair = []

    for i in alpha:
        pair.append(i + i)

    print(len(s))

    while len(s) >= 2:
        for i in range(len(s)):
            temp = s[i:i+2]
            if temp in pair:
                s = s.replace(temp, "")
            #     print(f's = {s}')
            # else:
            #     print(s)
        
    return answer

print(solution(s))
'''


'''
def solution(s):
    # True, False
    answer = 1
    alpha = 'abcdefghijklnmopqrstuvwxyz'
    pair = []

    for i in alpha:
        pair.append(i + i)
    
    # print(pair)

    for i in range(len(s)):
        temp = s[i:i+2]
        # if len(temp) == 2:
        if temp in pair:
            s = s.replace(temp, "")
            # print(s)
        else:
            if s in pair:
                answer = 1
            else:
                answer = 0

    return answer

print(solution(s))
'''