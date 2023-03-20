#test1에서만 맞는 코드
# def solution(prices):
    
#     n = len(prices)
    
#     answer = []
    
#     for i in range(n):
#         cnt = 0
#         for j in range(i+1, n):
#             if prices[i]<prices[j]:
#                 cnt += 1
#         answer.append(cnt)  
#     return answer

#질문하기에서 찾은 코드.
def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        # 끝까지 안떨어지는 경우
        time = len(prices) - i -1
        # 중간에 떨어지는 경우
        for i_p in range(i+1,len(prices)):
            if prices[i_p] < prices[i]:
                time = i_p - i
                break
        answer.append(time)
    answer.append(0)
    return answer