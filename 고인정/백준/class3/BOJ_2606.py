# 바이러스

cnt = 0
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

com = int(input())
line = int(input())

graph = [[] * (com+1) for _ in range(com+1)]

for _ in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (com+1)
dfs(1)
print(cnt)

# https://chanos.tistory.com/m/entry/%EB%B0%B1%EC%A4%80-2606%EB%B2%88-%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-DFS%EC%99%80-BFS-%EC%B0%A8%EC%9D%B4

'''
com = int(input())
line = int(input())

graph = [[] * (com+1) for _ in range(com+1)]

# print(f'graph = {graph}')

for _ in range(line):
    a, b = map(int, input().split())
    # print(f'graph[{a}] = {graph[a]}')
    # print(f'graph[{b}] = {graph[b]}')
    graph[a].append(b)
    graph[b].append(a)

# print(f'graph = {graph}')

cnt = 0
visited = [0] * (com+1)
# print(f'visited = {visited}')

def dfs(start):
    global cnt
    visited[start] = 1
    # print(visited)
    for i in graph[start]:
        # print(f'i = {i}')
        # print(f'visited[{i}] = {visited[i]}')
        if visited[i] == 0:
            dfs(i)
            # print(f'visited[{i}] = {visited[i]}')
            cnt += 1
            # print(f'cnt = {cnt}')

dfs(1)
print(cnt)

# https://jiwon-coding.tistory.com/93

# https://www.youtube.com/watch?v=7C9RgOcvkvo&t=604s
'''


'''
# 컴퓨터의 수
com = int(input())

# 직접 연결되어 있는 컴퓨터 쌍의 수
line = int(input())

# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 바이러스에 걸리게 되는 컴퓨터의 수
com_line = []
stack = set()

for i in range(line):
    com_line.append(input().split())
    if com_line[i][0] == '1':
        stack.add(com_line[i][1])
    elif com_line[i][0] in stack:
        stack.add(com_line[i][1])


# print(com_line)
# print(stack)
print(len(stack))
'''