# 다음 큰 숫자

# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.


def solution(n):
    answer = 0
    base2_n = bin(n)[2:]
    # print(base2_n)
    cnt_n1 = base2_n.count('1')
    # print(cnt_n1)

    for i in range(n+1, 1000001):
        base2_i = bin(i)[2:]
        cnt_i1 = base2_i.count('1')
        if cnt_n1 == cnt_i1:
            answer = i
            break
    
    return answer

print(solution(78))




'''def Base2(n):
    answer = ''

    while n != 1:
        print(f'n = {n}')
        n = n // 2
        answer += str(n % 2)
        print(f'n = {n}, answer = {answer}')
    
    n = n // 2
    answer += str(n % 2)
    print(f'n = {n}, answer = {answer}')

    return answer[::-1]

print(Base2(78))'''