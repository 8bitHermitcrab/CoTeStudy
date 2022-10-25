# 2×n 타일링 2

n = int(input())

n_list = [0, 1, 3, 5, 11, 21]

if n >= 6:
    for i in range(6, n+1):
        n_list.append(n_list[i-2] * 2 + n_list[i-1])

cnt = n_list[n]

answer = cnt % 10007

print(answer)

# https://cijbest.tistory.com/21

# n_list = [1, 1, 3, 5, 11, 21]

# n_list[0] = 1
# n_list[1] = 1

# print(n_list)

# if n >= 2:
#     for i in range(2, n+1):
#         # n_list.append(i + n_list[i-1] + n_list[i-2])
#         # n_list.append(sum(n_list[:i])+1)
#         # n_list.append(n_list[i-2] * 2 + n_list[i-1])
#         n_list[i] = n_list[i-1] + 2 * n_list[i-2]