# 두 정수 사이의 합


a = 3
b = 5

answer = 0

if a < b:
    for i in range(a, b+1):
        answer += i 
elif a > b:
    for i in range(b, a+1):
        answer += i 
else:
    answer = a

print(answer)