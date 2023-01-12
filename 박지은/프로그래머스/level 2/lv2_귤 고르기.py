# https://blog.naver.com/sara100410/222941955962
# https://blog.naver.com/kkh898/222845111631

from collections import Counter

def solution(k, tangerine):
    answer = 0
    c = Counter(tangerine)
    cnt = 0
    
    #print(c)
    
    for x in c.most_common():
        #print(x)
        #귤 갯수 -> x[1]
        cnt += x[1]
        #print(cnt)
        answer += 1
        if cnt >= k:
            break
    return answer