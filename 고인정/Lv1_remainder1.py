# 나머지가 1이 되는 수 찾기

n = 10

answer = 0
for i in range(1, n+1):
    if n % i == 1:
        answer = i
        break