#이해 못했어여ㅕㅕㅕ
#https://blog.naver.com/willyouspeedup/222859677202
import sys
input = sys.stdin.readline

n=int(input())
dp=[[0,0]]

for i in range(n):
    a=int(input())
    dp.append([a,a])


if n==1:
    print(dp[1][0])
    sys.exit()
    
for i in range(2,n+1):
    dp[i][0]+=max(dp[i-2])
    dp[i][1]+=dp[i-1][0]
#print(dp)
print(max(dp[n]))


