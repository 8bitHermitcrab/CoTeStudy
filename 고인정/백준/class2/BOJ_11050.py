# 이항 계수 1

import math

n, k = map(int, input().split())

# n!
# ----
# r!(n-r)!


answer = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
print(answer)

'''
n_res = 1
k_res = 1
n_k_res = 1

for i in range(1, n+1):
    n_num *= i
for j in range(1, k+1):
    k_num *= j
for m in range(1, ((n-k)+1)):
    n_k_num *= m
    
answer = n_res / (k_res * n_k_res)

print(answer)'''