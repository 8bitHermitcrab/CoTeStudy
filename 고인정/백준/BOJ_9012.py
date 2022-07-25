# 괄호

t = int(input())

ps = []

# 올바른 괄호 문자열(VPS) 확인
def VPS(ps):
    stack = []
    cnt = 0
    for i in ps:
        if i == '(':
            stack.append(i)
            cnt += 1
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
                cnt += 1
            else:
                stack.append(i)
                cnt += 1
                break

    if len(stack) == 0 and cnt != 0:
        print('YES')
    else:
        print('NO')
    return

for _ in range(t):
    ps.append(input().split())

for i in ps:
    VPS(i[0])
