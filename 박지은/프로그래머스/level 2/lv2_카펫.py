def solution(brown, yellow):
    s = brown + yellow
    answer = []
    #a = 가로
    #b = 세로
    #2a+2b+4 = brown
    
    for i in range(1, s+1):
        if s % i == 0:
            a = i
            b = int(s/i)
            if a>=b:
                if 2*a + 2*b - 4 == brown:
                    answer = [a, b]
    
    return answer