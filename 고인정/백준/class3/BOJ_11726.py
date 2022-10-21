# 2×n 타일링

n = int(input())

n_list = [0, 1, 2, 3]

if n >= 4:
    for i in range(4, n+1):
        n_list.append(n_list[i-2]+n_list[i-1])

# print(f'n_list = {n_list}')

cnt = n_list[n]

answer = cnt % 10007

print(answer)

# https://dev-note-97.tistory.com/146