# 나무 자르기

n, m = map(int, input().split())

h = list(map(int, input().split()))

print(h)

print(f'm = {m}')

start, end = 1, max(h)

while start <= end:
    print(f'----- start, end = {start}, {end} ------')
    mid = (start + end) // 2
    print(f'mid = {mid}')

    tree = 0
    for i in h:
        if i >= mid:
            tree += i - mid

    print(f'tree = {tree}')

    if tree >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# https://claude-u.tistory.com/446

# if m > 0:
#     wood = 1
#     print(f'max(h) = {max(h)}')
#     while wood != m:
#         for i in h:
#             if i > high:
#                 wood += (i - high)
#             else:
#                 wood += 0

#         high -= 1

# print(high-1)
