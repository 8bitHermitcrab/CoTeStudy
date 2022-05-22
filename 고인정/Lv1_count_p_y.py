# 문자열 내 p와 y의 개수


s = "pPoooyY"
answer = True
p_cnt = 0
y_cnt = 0
# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
for i in range(len(s)):
    if 'y' == s[i]:
        y_cnt += 1
    elif 'Y' == s[i]:
        y_cnt += 1
    elif 'P' == s[i]:
        p_cnt += 1
    elif 'p' == s[i]:
        p_cnt += 1

if y_cnt == p_cnt:
    answer = True
else:
    answer = False