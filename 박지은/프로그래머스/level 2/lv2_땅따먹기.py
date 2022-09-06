#https://blog.naver.com/idmanddang/222719481875
def solution(land):
    
    for i in range(1, len(land)):
        for j in range(4):
            #바로 전 행에서 해당 열이 아닌 값 중 최대값 구하기
            max_sum = max(land[i-1][:j] + land[i-1][j+1:])
            #합의 최대값 더해주면서 갱신하기
            land[i][j] = land[i][j] + max_sum
            
    #마지막 행의 최대값이 정답
    answer = max(land[-1])

    return answer