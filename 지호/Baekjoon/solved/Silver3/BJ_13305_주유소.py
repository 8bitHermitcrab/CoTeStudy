# 100점 (성공)
n = int(input())
length = list(map(int, input().split()))
oil = list(map(int, input().split()))

cost = 0
oil_money = oil[0]

for i in range(n-1):
  if oil_money > oil[i]:
    oil_money = oil[i]
  cost += length[i]*oil_money

print(cost)