# N과 M (4)

n, m = map(int, input().split())
stack = []

def dfs(cnt, idx):
    if cnt-1 == m:
        print(' '.join(map(str, stack)))
        return

    for i in range(idx, n+1):
        stack.append(i)
        dfs(cnt+1, i)
        stack.pop()
dfs(1, 1)

# https://zidarn87.tistory.com/336