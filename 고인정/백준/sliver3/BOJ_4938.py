# 베르트랑 공준

def getPrime(n):
    nums = [True] * (n)
    for i in range (2, int(n**0.5) + 1):
        if nums[i] == True:
            for j in range(2*i, n, i):
                nums[j] = False
    return [i for i in range(2, n) if nums[i] == True]

while True:
    n = int(input())

    if n == 0:
        break
    prime_list = getPrime(2*n + 1)
    answer_list = [num for num in prime_list if num > n]
    print(len(answer_list))



'''
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
'''

'''
# 에라토스테네스의 체
def isPrime(n):
    nums = [False, False] + [True] * n-1
    primes = []

    for i in range(2, n+1):
        if primes[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                primes[j] = False


n = int(input())

answer = []

while True:
    n = int(input())
    if n == 0:
        break
    
    for i in range(2*n + 1):
        if isPrime(i) == True:
            answer.append(i)
    print(len(answer))
'''