#https://blog.naver.com/idmanddang/222807014109

# 올바른 괄호의 경우, ([{}]), ()[{}], [](){} 등과 같이 열리는 괄호 뒤에 닫히는 괄호가 있는 형태.
# 여러겹의 괄호의 경우에도 안쪽 괄호부터 닫혀야 하므로 '()', '{}', '[]'를 포함, 이를 반복해서 제거하면 빈 문자열 '' 이 됩니다. 


# i칸만큼 회전한 괄호를 ss라 하면, ss = s[i:] + s[:i]

# 회전 후, while문내에서 ss를 temp에 저장하고 

# if문으로 '()', '{}', '[]' 중 하나라도 포함하면 이를 지우도록 함.

# temp와 if문을 통해 괄호가 지워진 ss가 같다면, 열고 닫히는 괄호가 없어서 지우지 않은 것이므로  while문을 break.

# 남은 ss가 빈 문자열 ''이면 올바른 괄호이므로 answer += 1을 해줌.

# for 문으로 i칸만큼 회전하는 것을 range(len(s)) 범위에서 해주면, answer가 업데이트 되며 정답!

def solution(s):
    answer = 0
    for i in range(len(s)):
        #i만큼 회전한 괄호
        ss = s[i:] + s[:i]
        while True:
            temp = ss
            #지우기
            if '()' in ss:
                ss = ss.replace('()', '')
            elif '{}' in ss:
                ss = ss.replace('{}', '')
            elif '[]' in ss:
                ss = ss.replace('[]', '')
            if temp == ss:
                break
        if ss == '':
            answer += 1
    return answer