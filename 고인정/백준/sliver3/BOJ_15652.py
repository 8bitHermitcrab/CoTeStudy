# N과 M (4)

n, m = map(int, input().split())

stack = []

def dfs(start):
    if len(stack) == m:
        print(' '.join(map(str, stack)))

    for i in range(start, n+1):
        stack.append(i)
        dfs(i)
        stack.pop()
dfs(1)
