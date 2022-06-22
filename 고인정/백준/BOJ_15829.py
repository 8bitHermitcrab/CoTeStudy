# Hashing

L = int(input())

# mod M
M = 1234567891

r = 31
user_input = input()

answer = 0

# alpha = 'abcdefghijklmnopqrstuvwxyz'


# ( l-1((l-1)-1)/2 ) * a * 31 mod 1234567891
for i in range(L):
    answer += (ord(user_input[i]) - 96) * (31 ** i)
print(answer % M)


# https://claude-u.tistory.com/432