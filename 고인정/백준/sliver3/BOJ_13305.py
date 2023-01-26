# 주유소

import sys
input = sys.stdin.readline

n = int(input())
way = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_price = way[0] * cost[0]
min_cost = cost[0]

for i in range(1, n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    min_price += min_cost * way[i]

print(min_price)