# 1로 만들기

# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

x = int(input())
dp = [0] * (x+1)

# print(dp)

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    print(f'dp[{i}] = {dp[i]}')

    if i % 2 == 0:
        print(dp[i], dp[i//2]+1)
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        print(dp[i], dp[i//3]+1)
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp)
print(dp[x])

# https://jae04099.tistory.com/199



'''
# cnt = 0

for _ in range(x):
    if x % 2 == 0:
        x = x // 2
        cnt += 1
    elif x % 3 == 0:
        x = x // 3
        cnt += 1
    else:
        x -= 1

print(cnt)
'''