# 수박수박수박수박수박수?


# n = 3
n = 4

if n == 1:
    answer = '수'
elif n % 2 == 0:
    answer = '수박' * (n//2)
elif n % 2 == 1:
    answer = '수박' * ((n-1) // 2) + '수'

print(answer)