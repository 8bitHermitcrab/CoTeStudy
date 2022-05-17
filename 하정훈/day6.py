# 정수의 제곱근

def solution(n):
  x = n**(1/2)
  if n % x == 0:
    return int((x+1)**2)

  else:
    return -1

def solution(n):
    answer = 0
    
    r_n = n ** (1/2) # 제곱근

    if r_n == int(r_n):
        answer = (r_n + 1)*(r_n + 1)
    else : 
        answer = -1
        
    return answer