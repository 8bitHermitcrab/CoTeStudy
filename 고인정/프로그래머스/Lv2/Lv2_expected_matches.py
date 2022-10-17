# 예상 대진표

# 단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.

# 4     7
# 1(2)4 5(6)7
# 12 34 56 78

n = 8
a = 4
b = 7

# 2  3
# 12 34

# n = 4
# a = 2
# b = 4

def solution(n,a,b):
    answer = 0

    while a != b:
        answer += 1

        # 1을 더해서 2로 나누었을 때, 자리수를 맞춰줌
        # 예) 1, 2의 경우는 2, 3으로 나누었을 때 몫이 1, 1

        print(f'a, b = {a}, {b}')
        a, b = (a+1)//2, (b+1)//2
        print(f'a+1//2, b+1//2 = {a}, {b}')

    return answer

print(solution(n,a,b))

# https://eda-ai-lab.tistory.com/m/500


'''
def solution(n,a,b):
    # 라운드
    answer = 0

    matches = [i for i in range(1, n+1)]
    
    stack = []

    for i in range(0, len(matches)+2, 2):
        print(f'matches[i-2:{i}] = {matches[i-2:i]}')
        if a in matches[i-2:i]:
            stack.append(a)
        elif b in matches[i-2:i]:
            stack.append(b)
        else:
            answer += 1
    print(f'stack = {stack}')
    print(f'matches2 = {matches}')

    return answer

print(solution(n,a,b))
'''