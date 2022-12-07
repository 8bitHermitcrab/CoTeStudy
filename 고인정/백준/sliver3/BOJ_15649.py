# N과 M (1)

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

n, m = map(int, input().split())

s = []

# f = [1, 2, 3]
# print(' '.join(map(str, f)))

# 백트래킹 문제

def dfs():
    # print(f'm, len(s) = {m}, {len(s)}')
    
    # 깊이 정해주기
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    # print(f's = {s}')

    # 결과값 정해주기
    for i in range(1, n+1):
        # print(f's = {s}')
        if i not in s:
            s.append(i)
            # print(f's_append = {s}')

            # recall
            dfs()
            # print(f's_dfs = {s}')
            s.pop()
            # print(f's_pop = {s}')

dfs()

# https://jiwon-coding.tistory.com/21

'''
if m > 1:
    for i in range(1, n+1):
        for j in range(1, m+1):
            print(i, j)
else:
    for i in range(1, n+1):
        print(i)
'''