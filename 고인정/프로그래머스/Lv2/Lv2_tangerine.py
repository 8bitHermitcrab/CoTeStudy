# 귤 고르기

def solution(k, tangerine):
    answer = 0
    cnt = dict()
    for i in tangerine:
        try:
            cnt[i] += 1
        except:
            cnt[i] = 1
    k_list = sorted(list(cnt.items()), key=lambda x:x[1], reverse=True)
    for i in k_list:
        k -= i[1]
        answer += 1
        if k <= 0:
            break
    return answer