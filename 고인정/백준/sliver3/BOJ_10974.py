# 모든 순열

n = int(input())

visited = [0] * n

def dfs(depth):
    if depth == n:
        print(*visited)
    else:
        for i in range(n):
            if i+1 in visited:
                continue
            visited[depth] = i + 1
            dfs(depth + 1)
            visited[depth] = 0

dfs(0)

# https://velog.io/@y7y1h13/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-10974%EB%B2%88-%EB%AA%A8%EB%93%A0-%EC%88%9C%EC%97%B4python
