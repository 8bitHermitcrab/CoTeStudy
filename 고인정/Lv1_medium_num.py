# 가운데 글자 가져오기

s = "qwer"
answer = ''

m = len(s) // 2

if len(s) % 2 == 0:
    answer = s[m-1:m+1]
else:
    answer = s[m]