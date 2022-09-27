# 바이러스

com = int(input())
line = int(input())

graph = [[] * com for _ in range(com+1)]

print(f'graph = {graph}')

for _ in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(f'graph = {graph}')

cnt = 0
visited = [0] * (com+1)
print(f'visited = {visited}')

def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)

# https://jiwon-coding.tistory.com/93


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