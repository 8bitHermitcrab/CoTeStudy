#

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

# lottos = [45, 4, 35, 20, 3, 9]
# win_nums = [20, 9, 3, 45, 4, 35]

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0

    cnt_zero = lottos.count(0)
    for i in win_nums:
        if i in lottos:
            cnt += 1
            print(f'cnt = {cnt}')
            print(f'cnt_zero = {cnt_zero}')
            print(f'rank[cnt_zero + cnt]')
    
    # 순위 당첨
    # 1 = 6개 일치
    # 2 = 5개 일치
    # 3 = 4개 일치
    # 4 = 3개 일치
    # 5 = 2개 일치
    # 6 = 1개 일치
    # 6 = 0개 일치
    answer = [rank[cnt_zero + cnt], rank[cnt]]

    return answer


print(solution(lottos, win_nums))




'''def solution(lottos, win_nums):
    # 등수, 번호 개수
    answer = []
    rank = 6
    cnt = 0
    # 전부 0일 때
    # lottos = [0, 0, 0, 0, 0, 0]
    if sum(lottos) == 0:
        rank = 1
        cnt = 6
        answer = [rank, cnt]
    
    # 0이 하나라도 있을 때
    cnt_zero = lottos.count(0)
    if cnt_zero > 0:
        for i in lottos:
            for j in win_nums:
                if i == j:
                    cnt += 1
                    rank -= 1
        rank = rank - (cnt_zero - 1)
        cnt = cnt + (cnt_zero + 1)
        answer = [rank, cnt]
        # print(f'cnt_zero = {cnt_zero}')
        
    # 0이 없을 때
    # lottos = [1~6], [40~45]
    if sum(lottos) >= 21 and sum(lottos) <= 255:
        for i in lottos:
            for j in win_nums:
                if i == j:
                    cnt += 1
                    rank -= 1
        answer = [rank, cnt] 
    return answer'''

    # https://datahub.tistory.com/12