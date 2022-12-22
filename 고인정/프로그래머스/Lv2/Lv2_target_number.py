# 타겟 넘버

numbers = [1, 1, 1, 1, 1]
target = 3



def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer

def dfs(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        # print(numbers)
        if sum(numbers) == target:
            return 1
        else: return 0
    else:
        answer += dfs(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += dfs(numbers, target, depth+1)
        return answer

print(solution(numbers, target))

# https://velog.io/@timointhebush/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%83%80%EA%B2%9F-%EB%84%98%EB%B2%84-DFS-BFS-Python