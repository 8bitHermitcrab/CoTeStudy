#0 -> 최근에 재민이가 쓴 수를 지움
#모든 수를 받아 적은 후 그 수의 합을 구하기

import sys

input = sys.stdin.readline

N = int(input())

num_list = []

for _ in range(N):
    n = int(input())
    
    if n != 0:
        num_list.append(n)

    else:
        num_list.pop()

print(sum(num_list))






