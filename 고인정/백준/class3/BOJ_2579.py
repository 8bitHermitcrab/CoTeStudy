# 계단 오르기

# 밟은 계단이 "END - 1"일 경우 반드시 "END - 2" 계단을 밟으면 안 된다. - case_A
# 밟은 계단이 "END - 2"일 경우 그 전 계단은 신경 쓰지 않는다. - case_B

# 계단의 개수
t = int(input())

step =  [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(t):
    step[i] = int(input())

dp[0] = step[0]
dp[1] = step[0] + step[1]
dp[2] = max(step[1] + step[2], step[0] + step[2])

for i in range(3, t):
    dp[i]= max(dp[i-2] + step[i], dp[i-3] + step[i] + step[i-1])

print(dp[t - 1])

# https://pacific-ocean.tistory.com/149


'''
# https://sungmin-joo.tistory.com/18

# 계단의 개수
t = int(input())

# answer = 0
step =  [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(t):
    step[i] = int(input())

# print(step)
# print(step[0])
dp.append(step[0])
# print(step)
# print(step[0]+step[1], step[1])
dp.append(max(step[0]+step[1], step[1]))
# print(step[0]+step[2], step[1]+step[2])
dp.append(max(step[0]+step[2], step[1]+step[2]))
# print(step)

for i in range(3, t):
    dp.append(max(dp[i-2] + step[i], dp[i-3] + step[i] + step[i-1]))

print(dp.pop())
'''