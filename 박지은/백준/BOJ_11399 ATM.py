#ATM
# [3, 1, 4, 3, 2] -> [1, 2, 3, 3, 4]

# 1 = 1
# 1+2 = 3
# 1+2+3 = 6
# 1+2+3+3 = 9
# 1+2+3+3+4 = 13

# 1 + 3 + 6 + 9 + 13 = 32


import sys
input = sys.stdin.readline

N = int(input())

times = list(map(int,input().split()))
#오름차순 정렬
times.sort()

result = 0

for i in range(1,N):
    times[i] += times[i-1] 

print(sum(times))
