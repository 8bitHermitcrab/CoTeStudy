# 문자열 집합

n, m = map(int, input().split())

cnt = 0

s = []
s_list = []

for _ in range(n):
    i = input()
    s.append(i)

for _ in range(m):
    j = input()
    s_list.append(j)

print(s)
print(s_list)

for i in s_list:
    if i in s:
        cnt += 1

print(cnt)