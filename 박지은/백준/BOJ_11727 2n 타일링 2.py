#221027
#https://my-coding-notes.tistory.com/182

#1. n-1의 모든 경우의 수 맨 끝에 세로 타일 하나를 둔다
#2. n-2의 모든 경우의 수 맨 끝에 가로 타일 두 개, 혹은 정사각형 하나를 둔다.

#dp[n] = dp[n-1] + dp[n-2]*2

#다이나믹 프로그램...이해를 잘 못하게쒀요...

import sys
input = sys.stdin.readline
dp = [1,3]
n = int(input())
while(len(dp) < n):
    dp.append((dp[-1]+dp[-2]*2)%10007)
print(dp[n-1])