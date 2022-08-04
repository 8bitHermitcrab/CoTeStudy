# https://blog.naver.com/idmanddang/222714094541

def solution(n):
    Fibonacci = [0, 1]
    for i in range(2, n+1):
        Fibonacci.append(Fibonacci[i-1] + Fibonacci[i-2])
        
    return Fibonacci[n]%1234567