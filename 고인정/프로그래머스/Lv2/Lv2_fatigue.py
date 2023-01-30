# 피로도

k = 100
dungeons = [[80, 8], [90, 9], [100, 10]]

# def solution(k, dungeons):
#     answer = 0
#     dungeons = sorted(dungeons, key=lambda x: ((x[1] + x[0])/x[0], x[1]))
#     for x, y in dungeons:
#         if k >= x:
#             k -= y
#             answer += 1        
#     return answer

ans = 0
N = 0
v = []

def dfs(k, cnt, dungeons):
    global ans
    if cnt > ans:
        ans = cnt

    for j in range(N):
        if k >= dungeons[j][0] and v[j] == 0:
            v[j] = 1
            dfs(k-dungeons[j][1], cnt+1, dungeons)
            v[j] = 0

def solution(k, dungeons):
    global N, v
    N = len(dungeons)
    v = [0] * N
    dfs(k, 0, dungeons)
    return ans

print(solution(k, dungeons))

# https://almighty-denver.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-lv2-%ED%94%BC%EB%A1%9C%EB%8F%84