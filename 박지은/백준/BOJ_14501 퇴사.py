# https://www.acmicpc.net/problem/14501
# 모르겠습니다ㅏㅏㅏㅏㅏㅏㅏ
#https://eggwhite0.tistory.com/111

N = int(input())

Ti = []
Pi = []

salary = [0 for i in range(N+1)]

sum = 0

for i in range(0, N):
    T, P = map(int, input().split())
    Ti.append(T)
    Pi.append(P)

for i in range(0, N):
    sum = max(sum, salary[i])

    if i + Ti[i] > N:
        continue

    salary[i + Ti[i]] = max(sum + Pi[i], salary[i + Ti[i]])

print(max(salary))