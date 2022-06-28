# 이상한 문자 만들기

s = "try hello world"

s_split = s.split(' ')
answer = ''

for i in range(len(s_split)):
    s_list = list(s_split[i])
    for j in range(len(s_list)):
        if j % 2 == 0:
            s_list[j] = s_list[j].upper()
            print(answer)
        else:
            s_list[j] = s_list[j].lower()
    s_split[i] = ''.join(s_list)
answer = ' '.join(s_split)

print(answer)

# https://somjang.tistory.com/entry/Programmers-%EC%9D%B4%EC%83%81%ED%95%9C-%EB%AC%B8%EC%9E%90-%EB%A7%8C%EB%93%A4%EA%B8%B0-Python