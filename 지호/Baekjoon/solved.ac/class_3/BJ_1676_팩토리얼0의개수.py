# 백준 1676번 : 팩토리얼 0의 개수

# 68초
n = int(input())
m = 1
answer = 0

for i in range(1, n+1):
  m *= i

for i in reversed(str(m)):
  if i == '0':
    answer += 1
  else:
    break

print(answer)



# 76초
import math

n = int(input())
answer = 0

m = math.factorial(n)

for i in reversed(str(m)):
  if i == '0':
    answer += 1
  else:
    break

print(answer)