# 다트 게임

dartResult = '1S2D*3T'
# dartResult = '1D2S#10S'


score = []
bonus = {'S':1, 'D':2, 'T':3}

dartResult = dartResult.replace('10', 'A')

for i in dartResult:
    if i.isdigit() or i == 'A':
        if i == 'A':
            i = 10
        else:
            i = int(i)
        score.append(i)
    elif i in ('S', 'D', 'T'):
        n = score.pop()
        score.append(n ** bonus[i])
    elif i == '#':
        score[-1] *= -1       
    elif i == '*':
        n = score.pop()
        if len(score):
            score[-1] *= 2
        score.append(2 * n)
        




answer = sum(score)

print(score)
print(sum(score))


'''
def solution(dartResult):
    stack = []
    dartResult = dartResult.replace("10", "A")
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    for i in dartResult:
        if i.isdigit() or i=='A':
            stack.append(10 if i == 'A' else int(i))
        elif i in ('S', 'D', 'T'):
            num = stack.pop()
            stack.append(num ** bonus[i])
        elif i == '#':
            stack[-1] *= -1
        elif i == '*':
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(2 * num)
    return sum(stack)
'''


# https://latte-is-horse.tistory.com/136