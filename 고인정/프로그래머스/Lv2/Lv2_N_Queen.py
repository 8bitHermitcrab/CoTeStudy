# N-Queen

n = 4
def solution(n):
    cases = [0] # shallow copy of the cases (list)
    def dfs(queens, next_queen):
        # 열 확인
        if next_queen in queens:
            return

        # 대각선 확인
        for row, column in enumerate(queens):
            print(f'row, column = {row, column}')
            h = len(queens) - row
            if next_queen == column + h or next_queen == column - h:
                return

        print(f'next_queen = {next_queen}')
        print(f'queens = {queens}')
        queens.append(next_queen)
        print(f'queens.append = {queens}')
        # 퀸 전부 배치
        if len(queens) == n:
            cases[0] += 1
            print(f'cases[0] = {cases[0]}')
            return

        for next_queen in range(n):
            dfs(queens[:], next_queen)

    for next_queen in range(n):
        queens = []
        dfs(queens, next_queen)
    return cases[0]
    
print(solution(4))

# https://davi06000.tistory.com/73









# 0:(1,1) 1:(2,1) 0:(3,1) 0:(4,1)
# 0:(1,2) 0:(2,2) 0:(3,2) 1:(4,2)
# 1:(1,3) 0:(2,3) 0:(3,3) 0:(4,3)
# 0:(1,4) 0:(2,4) 1:(3,4) 0:(4,4)

# 0:(1,1) 0:(2,1) 1:(3,1) 0:(4,1) 0:(5,1)
# 0:(1,2) 0:(2,2) 0:(3,2) 0:(4,2) 1:(5,2)
# 0:(1,3) 1:(2,3) 0:(3,3) 0:(4,3) 0:(5,3)
# 0:(1,4) 0:(2,4) 0:(3,4) 1:(4,4) 0:(5,4)
# 1:(1,5) 0:(2,5) 0:(3,5) 0:(4,5) 0:(5,5)

#  start
#  1,1
#  2,3
#  X

#  start
#  1,1
#  2,4
#  3,2
#  X

#  start
#  1,2
#  2,4
#  3,1
#  4,3

#  d = 4이면, 정답

# 대각선 체크
# col[i] - col[k] == abs(i - k)

# def n_queens(i, col):
#     n = len(col) - 1
#     if (promising(col, i)):
#         if (i == n):
#             print(col[1 : n + 1])
#         else:
#             for j in range(1, n + 1):
#                 col[i + 1] = j
#                 n_queens(col, i + 1)

# def promising(i, col):
#     k = 1
#     flag = True
#     while (k < 1 and flag):
#         # 같은 열인지, 같은 대각선인지 체크
#         if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
#             flag = False
#         k += 1
#     return flag


# n = 4
# col = [0] * (n + 1)
# n_queens(0, col)

'''
def n_queens (col, i):

    n = len(col) - 1
    if (promising(col, i)):
        if (i == n):
            print(col[1: n + 1])
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(col, i + 1)

def promising (col, i):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag

def solution(n):
    col = [0] * (n + 1)
    n_queens(col, 0)
    
print(solution(4))


# https://www.youtube.com/watch?v=z4wKvYdd6wM'''



