# 어린 왕자

# t
# x1, y1, x2, y2
# n
# cx, cy, cr

t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, cr = map(int, input().split())
        dis1 = (((x1 - cx) ** 2) + ((y1 - cy) ** 2)) ** 0.5
        dis2 = (((x2 - cx) ** 2) + ((y2 - cy) ** 2)) ** 0.5

        if (cr > dis1 and cr < dis2) or (dis1 > cr and dis2 < cr):
            cnt += 1
    print(cnt)

# https://pacific-ocean.tistory.com/108
