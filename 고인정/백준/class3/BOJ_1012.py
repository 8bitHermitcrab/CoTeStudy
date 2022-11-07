# 유기농 배추

import sys
sys.setrecursionlimit(10**6)
# 파이썬의 기본 재귀 깊이 제한은 1,000 
# 이 코드로 재귀 깊이 제한을 1,000,000으로 늘려준다

# https://fuzzysound.github.io/sys-setrecursionlimit

t = int(input())

# 상 : (x-1, y)
# 하 : (x+1, y)
# 좌 : (x, y-1)
# 우 : (x, y+1)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# DFS
def DFS(x, y):
    # 상 : (x-1, y)
    # 하 : (x+1, y)
    # 좌 : (x, y-1)
    # 우 : (x, y+1)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 4가지 방향 선택
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if mn_list[ny][nx] == 1:
                mn_list[ny][nx] = 0
                DFS(nx, ny)


for _ in range(t):
    # 가로m, 세로n, 배추 위치 개수k
    m, n, k = map(int, input().split())
    # print(t, m, n, k)

    mn_list = [[0] * m for _ in range(n)]

    cnt = 0

    for _ in range(k):
        # 배추 위치(x, y)
        x, y = map(int, input().split())
        mn_list[y][x] = 1

    print(f'mn_list = {mn_list}')

    # DFS
    for x in range(m):
        for y in range(n):
            # 배추가 있을 때
            if mn_list[y][x] == 1:
                # 인접해있는 배추 탐색
                DFS(x, y)
                # 탐색 완료시, 지렁이 추가
                cnt += 1

    print(cnt)

# https://hei-jayden.tistory.com/100

'''
# DFS
def search(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if mn_list[x][y] == 0:
        return
    
    # 탐색한 배추는 0으로 갱신
    mn_list[x][y] = 0

    # 상하좌우 탐색
    search(x-1, y)
    search(x+1, y)
    search(x, y-1)
    search(x, y+1)'''


# https://deep-learning-study.tistory.com/615



# mn_list = [[0, 0, 0, 0, 1], 
#           [0, 0, 0, 0, 0], 
#           [1, 1, 1, 1, 1]]