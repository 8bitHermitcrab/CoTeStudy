# DFS와 BFS

# 정점 n개, 간선 m개, 탐색시작 정점 번호v
n, m, v = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
print(f'graph = {graph}')

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

print(f'graph = {graph}')

# 방문 리스트 행렬
visited1 = [0] * (n+1)
visited2 = visited1.copy()
# print(f'visited1 = {visited1}')

def dfs(v):
    # 방문 처리
    visited1[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited1[i] == 0:
            dfs(i)
    return

def bfs(v):
    queue = [v]
    # 방문 처리
    visited2[v] = 1
    while queue:
        # 방문 노드 제거
        v = queue.pop(0)
        print(v, end= ' ')
        for i in range(1, n+1):
            if visited2[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                # 방문 처리
                visited2[i] = 1
    return

dfs(v)
# print(f'visited1 = {visited1}')
print()
bfs(v)
# print(f'visited2 = {visited2}')

# https://intrepidgeeks.com/tutorial/backup-python-no-1260-dfs-and-bfs-dfsbfs-basic-implementation-details