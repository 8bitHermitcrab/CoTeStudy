# 연속 부분 수열 합의 개수

def solution(elements):
    answer = set()
    
    elements_len = len(elements)
    elements = elements * 2
    
    for i in range(elements_len):
        for j in range(elements_len):
            answer.add(sum(elements[j:j+i+1]))
    return len(answer)

# https://velog.io/@kauthenticity/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%B0%EC%86%8D-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%95%A9%EC%9D%98-%EA%B0%9C%EC%88%98