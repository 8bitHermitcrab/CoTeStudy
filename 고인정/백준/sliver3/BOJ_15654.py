# n과 m (5)

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
visited = [False] * n
out_list = []

def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str,out_list)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            out_list.append(num_list[i])
            dfs(depth+1, n, m)
            out_list.pop()
            visited[i] = False
dfs(0, n, m)

# https://wlstyql.tistory.com/62