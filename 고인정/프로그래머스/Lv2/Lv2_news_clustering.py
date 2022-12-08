# [1차] 뉴스 클러스터링

# 자카드 유사도
# 합집합 수 / 교집합 수
# 공집합 = 1

# 중복 원소의 수
# 교집합 min(3, 5)
# 합집합 max(3, 5)

# str1 = 'FRANCE'
# str1 = 'handshake'
str1 = 'aa1+aa2'
# str1 = 'E=M*C^2'

# str2 = 'french'
# str2 = 'shake hands'
str2 = 'AAAA12'
# str2 = 'e=m*c^2'


def solution(str1,str2):
    
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    intersection = set(str1) & set(str2)
    union = set(str1) | set(str2)
    
    inter = sum([min(str1.count(word), str2.count(word)) for word in intersection])
    union = sum([max(str1.count(word), str2.count(word)) for word in union])

    if union ==0:
        return 65536
    return int(inter/union * 65536)


print(solution(str1, str2))

# https://journey-to-serendipity.tistory.com/25


# import math, re

'''
def solution(str1, str2):
    # 대문자로 변환
    up_str1 = str1.upper()
    up_str2 = str2.upper()
    # 특수문자, 공백 제거
    # new_str1 = re.sub(r'[^가-힣A-Z0-9]', '', up_str1)
    # new_str2 = re.sub(r'[^가-힣A-Z0-9]', '', up_str2)
    # 2글자씩 원소 만들기
    str1_list = []
    str2_list = []

    for i in range(len(up_str1)-1):
        if up_str1[i].isalpha() and up_str1[i+1].isalpha():
            str1_list.append(up_str1[i] + up_str1[i+1])
    for i in range(len(up_str2)-1):
        if up_str2[i].isalpha() and up_str2[i+1].isalpha():
            str2_list.append(up_str2[i] + up_str2[i+1])
        
    print(f'str1_list = {str1_list}')
    print(f'str2_list = {str2_list}')

    str1_cnt = dict()
    str2_cnt = dict()

    for j in range(len(str1_list)):
        try:
            str1_cnt[str1_list[j]] += 1
        except:
            str1_cnt[str1_list[j]] = 1
    
    for j in range(len(str2_list)):
        try:
            str2_cnt[str2_list[j]] += 1
        except:
            str2_cnt[str2_list[j]] = 1


    print(f'str1_cnt = {str1_cnt}')
    print(f'str2_cnt = {str2_cnt}')
    
    inter = []
    union = []

    for k in str1_cnt.keys():
        if k in str2_cnt.keys():
            inter.append(min(str1_cnt.get(k), str2_cnt.get(k)))
            union.append(max(str1_cnt.get(k), str2_cnt.get(k)))
        else:
            union.append(max(str1_cnt.get(k), str2_cnt.get(k)))

    # inter = list((str1_cnt & str2_cnt).values())
    # union = list((str1_cnt | str2_cnt).values())

    print(f'inter = {inter}')
    print(f'union = {union}')

    # 자카드 유사도
    # if len(union) == 0 and len(inter) == 0:
    #     return 65536
    # else:
    #     return int(len(inter) / len(union) * 65536)
    
    # 소수점 아래 버림
    # answer = math.trunc(answer * 65536)

# print(math.ceil(0.4 * 65536))

print(solution(str1, str2))




from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
            
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

# https://velog.io/@godiva7319/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2-1%EC%B0%A8-%EB%89%B4%EC%8A%A4-%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EB%A7%81-Python

print(solution(str1, str2))
'''