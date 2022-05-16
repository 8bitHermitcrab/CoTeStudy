# 자릿수 더하기

n = 123
answer = 0
str_n = str(n)
for i in range(len(str_n)):
    answer += int(str_n[i])

print(answer)