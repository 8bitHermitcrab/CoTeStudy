#https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-n%EC%A7%84%EC%88%98-%EA%B2%8C%EC%9E%84-Python

#10진수를 n진수로 바꿔주는 함수
def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        # q를 base로 변환
        # 즉, n진수의 다음 자리를 구함
        return convert(q, base) + temp[r]
    
def solution(n, t, m, p):
    answer = ''
    test = ''
    
    for i in range(m*t):
        test += str(convert(i, n))
        
    while len(answer) < t:
        answer += test[p-1]
        p += m
        
    return answer