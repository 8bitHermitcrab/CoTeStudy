# 실패율

def solution(N, stages):
    answer = {}
    len_stages = len(stages)
    
    # 1~N 스테이지까지
    for stage in range(1, N+1):
        if len_stages != 0:
            cnt = stages.count(stage)
            answer[stage] = cnt / len_stages
            # 스테이지를 깨지 못한 사람 빼기
            len_stages -= cnt
        # 실패율 0
        else:
            answer[stage] = 0
    # 내림차순 정렬
    return sorted(answer, key=lambda x : answer[x], reverse=True)



'''def solution(N, stages):
    answer = []
    
    # 실패율 dict
    fail_dict = {}
    # 1~N 스테이지까지
    for i in range(1, N+1):
        cnt = 0
        # 스테이지에 도달한 플레이어 수
        for j in range(len(stages)):
            # 1~N을 stages 값들과 비교
            if i < stages[j]:
                cnt += 1
        # i 스테이지의 실패율
        try:
            fail_dict[i] = stages.count(i) / cnt
        except ZeroDivisionError as zero:
            fail_dict[i] = 0
        if cnt == len(stages):
            fail_dict[i] = 1
    
    # value값으로 내림차순 정렬
    fail_dict = sorted(fail_dict.items(), key = lambda item: item[1], reverse = True)
          
        
    
    return fail_dict'''


    # https://it-garden.tistory.com/235
