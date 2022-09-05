#  백준 11047번 : 동전 0

n, k = map(int, input().split())

lst = []
answer = 0

for _ in range(n):
  coin = int(input())
  if coin <= k:
    lst.append(coin)
  else:
    break

for i in lst[::-1]:
  answer += k // i
  k = k % i

print(answer)