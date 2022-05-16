# 자연수 뒤집어 배열로 만들기

n = 12345
str_n = str(n)


answer = []
for i in range(len(str_n), 0, -1):
    answer.append(int(str_n[i-1]))

print(answer)