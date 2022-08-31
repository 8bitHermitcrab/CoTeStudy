import math

def solution(n, k):
    answer = 0
    
    num = ''
    
    while n>0:
        #k진수 문자열로만들기
        num = str(n%k) + num 
        n = n//k
    
    #0을 기준으로 나누기
    num = num.split('0')
    #int로 바꿔주기
    nums = [int(x) for x in num if x !='']
        
    #소수찾기
    for i in nums:
        if i != 1:
            add = 1
            for j in range(2, int(math.sqrt(i)) + 1):
                if i%j == 0:
                    add=0
                    break
            answer += add
    return answer