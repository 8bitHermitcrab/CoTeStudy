# 파도반 수열

t = int(input())

n = [int(input()) for _ in range(t)]
p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

print(f'max(n) = {max(n)}')

for i in range(11, max(n)+1):
    p.append(p[i-1] + p[i-5])

print(f'p = {p}')

for i in n:
    print(p[i])

# https://dojinkimm.github.io/problem_solving/2019/10/25/boj-9461-wave.html

'''
p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
# p1=1
# p1+p2=p4
# p2+p3=p5
# p3+p4=p6
# pn-3 + pn-2 = pn

for _ in range(t):
    n = int(input())
    if len(p) < n:
        for i in range(11, n+11):
            # print(f'i = {i}')
            p.append(p[i-3] + p[i-2])
    # print(f'p[n] = {p[n]}')
    print(p[n])
# print(f'p = {p}')
'''

