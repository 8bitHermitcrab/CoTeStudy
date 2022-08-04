# 피보나치 수

n = 5

# def solution(n):
    # f(0) = 0
    # f(1) = 1
    # f(n) = f(n-1) + f(n-2)
    # f(2) = f(2 - 1) + f(2 - 2)
    # f(2) = f(1)+f(0)
    # f(2) = 1+0

print(f'n = {n}')
f = [0, 1]

print(f'len(f) = {len(f)}')
while len(f) != n+1:
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    break
print(f)
answer = f[n] % 1234567
    # return answer

# print(solution(3))

print(f'answer = {answer}')