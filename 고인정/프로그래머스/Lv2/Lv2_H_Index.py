# H-Index

# 3
citations = [3, 0, 6, 1, 5]
# 논문 5개, 3(h1)편의 논문 3(cnt1)회 이상 인용
#         2(h2)편의 논문 3(cnt2)회 이하 인용

# 4
# citations = [10, 8, 5, 4, 3]
# 논문 5개, 4편의 논문 4회 이상 인용
#         2편의 논문 4회 이하 인용

# 3
# citations = [25, 8, 5, 3, 3]
# 논문 5개, 5편의 논문 3회 이상 인용
#         2편의 논문 3회 이하 인용

# https://en.wikipedia.org/wiki/H-index

# n편 중 h번 이상 인용된 논문이 h편 이상이고,
# h번 이하 인용되었다면, 최대값 h가 h-index

def solution(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        print(f'i, citation = {i, citation}')
        if i >= citation:
            return i
    return len(citations)

print(solution(citations))

# https://yunaaaas.tistory.com/56

'''
H-지수 구하는 방법
나의 h는 어떻게 구할 수 있을까? 
우측의 표와 같이 자신이 저널에 등재한 전체 논문중 많이 인용된 순으로 정렬한 후, 
피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자가 바로 나의 h가 됩니다. 
이 표에서는 10이 H-지수가 되는 것입니다. 
다시 말하여, 이 연구원은 논문 인용횟수가 10이 넘는 논문이 적어도 10편이 된다는 것을 의미합니다.

출처: [BRIC Bio통신원] [연구논문을 위한 핵심 10단계] H-지수(H-Index) 란 무엇인가? ( https://www.ibric.org/myboard/read.php?Board=news&id=270333 )
'''



'''
def solution(citations):
    
    h1_list = []
    # 인용수 i
    for i in citations:
        cnt = 0
        for j in citations:
            if i != 0 and i <= j:
                cnt += 1
        h1_list.append([i, cnt])
    
    print(f'h1_list = {h1_list}')

    h2_list = []
    # 인용수 i
    for i in citations:
        cnt = 0
        for j in citations:
            if i != 0 and i >= j:
                cnt += 1
        h2_list.append([i, cnt])
    
    print(f'h2_list = {h2_list}')

    stack = []

    for i in h1_list:
        for j in h2_list:
            if i == j:
                stack.append(i[1])

    answer = max(stack)

    return answer

print(solution(citations))
'''