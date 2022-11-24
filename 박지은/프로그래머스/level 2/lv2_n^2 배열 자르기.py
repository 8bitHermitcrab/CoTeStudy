#https://blog.naver.com/toddlf_1222/222927604602
def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        answer.append(max(divmod(i, n))+1)
        #print(answer)
    return answer