#https://blog.naver.com/hiro141611/222801515747
import math

def solution(progresses, speeds):
    answer = []
    max_day = 0
    for i in range(len(progresses)):
        #날짜 구하기(올림)
        day = math.ceil((100 - progresses[i])/speeds[i])
        
        #첫 번째(answer = []): 비교 대상체가 없기 때문에 max_day를 걸리는 날짜로 갱신하고 answer에 1 추가
        #   +
        #걸리는 날짜가 max_day보다 클 경우: 이전까지 비교하던 대상체보다 값이 커 배포가 불가능한 경우, max_day를 갱신하고 answer에 1을 추가
        
        #비교하는 대상보다 값이 작아 배포가 함께 가능함으로 answer 마지막 인덱스에 1을 더하여 갯수를 추가
        if answer == [] or day>max_day :
            answer.append(1)
            max_day = day
        
        #걸리는 날짜가 max_day보다 작거나 같은 경우
        else:
            answer[-1] += 1
        
    return answer