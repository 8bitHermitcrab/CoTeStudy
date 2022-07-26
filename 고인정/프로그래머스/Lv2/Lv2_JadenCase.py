# JadenCase 문자열 만들기

s = "3people unFollowed me"

def solution(s):
    s = s.split(" ")
    print(f's = {s}')
    for i in range(len(s)):
        print(f's[i][:1] = {s[i][:1]}')
        print(f's[i][1:] = {s[i][1:]}')
        s[i] = s[i][:1].upper() + s[i][1:].lower()
    return ' '.join(s)

'''
def solution(s):
    s = s.lower()
    answer = ''
    s_list = s.split()
    for i in s_list:
        if i[0].isalpha() == True:
            # print(f'i = {i}')
            upper_i = i[0].upper()
            i = upper_i + i[1:]
            # print(f'i = {i}')
            answer += (i + ' ')
        else:
            answer += (i + ' ')
    return answer[:-1]
'''

print(solution(s))


# https://wiselog.tistory.com/67