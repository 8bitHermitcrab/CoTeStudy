# 최소직사각형


sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]

w = []
h = []
for i in range(len(sizes)):
    if sizes[i][0] >= sizes[i][1]:
        # print(sizes[i][0])
        w.append(sizes[i][0])
        # print(f'w{i} = {w}')
        h.append(sizes[i][1])
        # print(f'h{i} = {h}')
    else:
        h.append(sizes[i][0])
        # print(f'w{i} = {w}')
        w.append(sizes[i][1])
        # print(f'h{i} = {h}')
    
print(w)
# [10, 12, 15, 14, 15]

print(h)
# [7, 3, 8, 7, 5]

print(max(w))
# 15
print(max(h))
# 8

w = max(w)
h = max(h)

print(w * h)
# 120

# https://velog.io/@guswl8280/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B5%9C%EC%86%8C-%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95-Python




'''n = len(sizes)
answer = 0
w = 0
h = 0
for i in range(n):
    sizes[i].sort()
    w = max(w, sizes[i][0])
    h = max(h, sizes[i][1])
    print(w, h)
    print(w * h)'''

# https://leeiopd.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level1-%EC%B5%9C%EC%86%8C%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC?category=944401?category=944401