# 3진법 뒤집기

n = 45


# 내장함수
answer = 0
result = ''

while n >= 1:
    n, b = divmod(n, 3)
    print(n, b)
    result += str(b)
    print(result)

answer = int(result, 3)
print(f'answer = {answer}')


# 로직
answer = 0
result = ''

while n >= 1:
    a = n % 3
    n //= 3
    result += str(a)

i = 0
for idx in range(len(result)-1, -1, -1):
    answer += int(result[idx]) * (3**i)
    i += 1

print(f'answer = {answer}')


# https://btfnswt.tistory.com/81