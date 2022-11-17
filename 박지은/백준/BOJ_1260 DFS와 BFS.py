#https://blog.naver.com/jungs-note/222919703251
#DFS와 BFS

import sys
from collections import deque
input = sys.stdin.readline

#N: 정점의 개수
#M: 간선의 개수
#V: 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())

#정점의 개수만큼 그래프 그리기
graph = []
for _ in range(N):
    graph.append([])

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

#방문
visited = []

#깊이 우선 탐색
def dfs(x):
    #방문 표시
    visited.append(x)
    for i in sorted(graph[x-1]):
        if i+1 not in visited:
            dfs(i+1)

dfs(V)
#dfs 출력
print(' '.join(list(map(str, visited))))

#너비 우선 탐색
def bfs(x):
    q = deque()
    #방문할 노드를 큐에 저장
    q.append(x)
    while q:
        #이번에 방문할 노드
        i = q.popleft()
        #i노드에 연결된 노드들
        for j in sorted(graph[i-1]):
            if j+1 not in visited:
                #다음에 방문할 노드로 지정
                q.append(j+1)
                visited.append(j+1)
bfs(V)
print(' '.join(list(map(str, visited))))
