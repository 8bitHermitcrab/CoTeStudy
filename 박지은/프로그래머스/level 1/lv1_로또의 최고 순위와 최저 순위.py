#https://blog.naver.com/charzim0611/222784270433
def solution(lottos, win_nums):
    answer = [6,6,5,4,3,2,1]
    lo = 0
    
    for i in lottos:
        if i in win_nums:
            lo += 1 
    
    no_num = lottos.count(0)
    
    a_lo = lo + no_num
    b_lo = lo
    
        
    return [answer[a_lo], answer[b_lo]]