#논문 n편 중 h번 이상 인용된 논문이 h편 이상
#나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 H-idnex
# def solution(citations):
#     citations.sort()
#     article_count = len(citations)
    
#     #이렇게 초기값 0을 먼저 설정하고 돌리니까 안됨
#     answer = 0
    
#     for i in range(article_count):
#         if citations[i] >= article_count-i:
#             answer = article_count-i
#     return answer

def solution(citations):
    citations.sort()
    article_count = len(citations)

    for i in range(article_count):
        if citations[i] >= article_count-i:
            return article_count-i
    return 0