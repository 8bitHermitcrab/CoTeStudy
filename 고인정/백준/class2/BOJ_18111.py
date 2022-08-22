# 마인크래프트

import sys

n, m, b = map(int, sys.stdin.readline().split())
# 땅
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 1e9 = 1*10^9 = 1,000,000,000
# INF = int(1e9)

# 층수
floor = 0

answer = sys.maxsize

for block in range(257):
    max_block, min_block = 0, 0

    for i in range(n):
        for j in range(m):

            if land[i][j] >= block:
                max_block += land[i][j] - block
            else:
                min_block += block - land[i][j]

    if max_block + b >= min_block:
        if min_block + (max_block * 2) <= answer:
            # 최저 시간
            answer = min_block + (max_block * 2)
            # 층수
            floor = block

print(answer, floor)

# https://www.youtube.com/watch?v=XjKhQ7Vcu3c

'''
import sys

n, m, b = map(int, sys.stdin.readline().split())
# 땅
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(graph)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]

answer = sys.maxsize
# print(answer)
# 9223372036854775807

idx = 0

# 0층부터 256층까지 반복
for target in range(257):
    max_target, min_target = 0, 0

    # 반복문을 통해 블록을 확인
    for i in range(n):
        for j in range(m):

            # 블록이 층수보다 더 크면
            if land[i][j] >= target:
                max_target += land[i][j] - target

            # 블록이 층수보다 더 작으면
            else:
                min_target += target - land[i][j]

    # 블록을 뺀 것과 원래 있던 블록의 합과 블록을 더한 값을 비교
    # 블록을 뺀 것과 원래 있던 블록의 합이 더 커야 층을 만들 수 있음.
    if max_target + b >= min_target:
        # 시간 초를 구하고 최저 시간과 비교 
        if min_target + (max_target * 2) <= answer:
        	# 0부터 256층까지 비교하므로 업데이트 될수록 고층의 최저시간
            answer = min_target + (max_target * 2) # 최저 시간
            idx = target # 층수

print(answer, idx)

# https://fre2-dom.tistory.com/457

'''

'''# 1번 작업 : 2초
remove_block = 2
# 2번 작업 : 1초
build_block = 1

block = []

# 좌표
xy = dict()

for _ in range(n):
    block.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        xy[(i, j)] = block[i][j]

print(f'xy = {xy}')

start, end = 0, max(xy.values())

print(f'start, end = {start}, {end}')

# 인벤토리에 블럭이 없을 때
if b == 0:

else:'''