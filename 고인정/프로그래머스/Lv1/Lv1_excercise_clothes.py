# 체육복

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    _reserve =  list(set(reserve) - set(lost)) 
    _lost =  list(set(lost) - set(reserve)) 
    
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
            
    answer = n - len(_lost)
    
    return answer