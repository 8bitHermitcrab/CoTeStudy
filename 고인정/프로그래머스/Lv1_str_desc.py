# 문자열 내림차순으로 배치하기


s = "Zbcdefg"

answer = ''

num = []
s_list = []

for i in range(len(s)):
    num.append(ord(s[i]))
print(num)
for i in range(len(s)):
    s_list.append(chr(num[i]))
print(s_list)

s_list.sort(reverse=True)
print(s_list)
answer = "".join(s_list)

print(answer)