#내가 짠 코드 -> 시간초과
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

nums = list(map(int, input().split()))

for i in range(M):
    x, y = map(int, input().split())
    sum = 0
    for j in range(x-1,y):
        sum += nums[j]
    print(sum)

#시간초과나서 검색, 이것도DP구나ㅏ
#https://blog.naver.com/wldlwn12/222903765478
import sys
input = sys.stdin.readline
N , M = map(int, input().split())

data = list(map(int, input().split()))

sumv = [0]*100001

for i in range(1,N+1):
    sumv[i] = sumv[i-1]+data[i-1]
#print(sumv)
for _ in range(M):
    a,b = map(int, input().split())
    print(sumv[b]-sumv[a-1])
