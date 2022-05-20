# 소수 찾기

n = 10
answer = 0


'''def is_prime_num(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True'''

a = [False, False] + [True]*(n-1)
prime_list = []

for i in range(2, n+1):
    if a[i]:
        prime_list.append(i)
        answer += 1
        for j in range(2*i, n+1, i):
            a[j] = False

print(answer)


# 에라토스테네스의 체
# https://iambeginnerdeveloper.tistory.com/121
# https://wikidocs.net/21638