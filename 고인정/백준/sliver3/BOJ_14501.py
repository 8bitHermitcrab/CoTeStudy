# 퇴사

# n+1일에 퇴사
# 남은 n일 동안 최대한 많은 상담

'''
 시간 복잡도: O(n^2)
 공간 복잡도: O(n)
 사용한 알고리즘: 동적 계획법(bottom-up, tabulation)
 사용한 자료구조: 배열
'''

'''
 t는 일을 완료하는데 걸리는 기간
 p는 일을 완료하고 받을 수 있는 금액

 d[n]은 n+1에 받을 수 있는 최대 금액을 의미합니다.
 아래의 예시에서 1일에 일을 하면 3일동안 일을 하기 때문에 4일에 금액을 받습니다.
   1  2  3  4
 t 3  5  1  1
 p 10 20 10 20
 d 0  0  0  10
'''

# 1. 입력
n = int(input())

t = [0]
p = [0]
# n + 1일 까지 계산합니다.
dp = [0] * (n+2)
result = 0

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# 2. DP (bottom-up) 수행
for i in range(1, n+2):
    for j in range(1, i):
        # 1) j 번째 날에서 일을 안하고 i 번째 날까지 온 경우(j < i)
        dp[i] = max(dp[i], dp[j])

        # 2) j 번째 날에서 t[j] 기간 동안 일을하고 보상을 p[j] 받은 경우
        # 그 보상은 j + t[j] 날 받습니다.
        if j + t[j] == i:
            dp[i] = max(dp[i], dp[j] + p[j])

    # 3) 최대값을 갱신해줍니다.
    result = max(result, dp[i])

# 3. 출력
print(result)


# https://velog.io/@skyepodium/%EB%B0%B1%EC%A4%80-14501-%ED%87%B4%EC%82%AC-exjyfr5vgj



'''

# n = 7
# [3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]
# [3, 10] + [1, 20] + [2, 15] = 45

n = int(input())

# dp = [0, 1, 2, ... n]
dp = [0] * (n+1)

# 1, 4, 5일 / 

# 시간 t, 돈 p
for i in range(n):
    t, p = map(int, input().split())
    if t <= n:
        if dp[t] == 0 or dp[t] > p:
            dp[t] = p

print(dp)
'''