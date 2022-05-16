# 이상한 문자 만들기

s = "try hello world"

s_s = s.split()
print(s_s)

for i in range(len(s_s)):
    print(len(s_s))
    print(f'i = {i}')
    for j in range(len(s_s[i])+1):
        if j % 2 == 1:
            s_s = s_s[i][j].upper()
        

print(s_s)