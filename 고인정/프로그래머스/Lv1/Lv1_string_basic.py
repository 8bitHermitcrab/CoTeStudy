# 문자열 다루기 기본

s = "a234"

answer = True
s_list = []
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
cnt = 0

if len(s) == 4 or len(s) == 6:
    for i in range(len(s)):
        s_list.append(s[i])
        if s_list[i] in num:
            cnt += 1

    if cnt == len(s):
        answer = True
    else:
        answer = False
else:
    answer = False
        



print(answer)