# ATM

n = int(input())

p = list(map(int, input().split()))

print(p)
p.sort()

print(p)

for i in range(n):
    if i > 0:
        p[i] = p[i-1] + p[i]

print(p)
print(sum(p))