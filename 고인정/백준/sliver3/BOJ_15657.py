# n과 m (8)

n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
# print(num_list)
str_num = ''.join(str(i) for i in num_list)
# print(str_num)

temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(start, n):
        temp.append(num_list[i])
        dfs(i)
        temp.pop()
dfs(0)

# https://honggom.tistory.com/110