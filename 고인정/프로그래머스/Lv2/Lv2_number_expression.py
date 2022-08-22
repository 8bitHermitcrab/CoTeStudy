# 숫자의 표현

n = 15

def solution(n):
    # 개수 세기
    answer = 0
   
    for i in range(1, n+1):
        # sum
        s = 0
        for j in range(i, n+1):
            s += j
            if s == n:
                answer += 1
                break
            elif s > n:
                break

    return answer

print(solution(n))

# https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%AB%EC%9E%90%EC%9D%98-%ED%91%9C%ED%98%84-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9CLevel-2

'''
max_n = 10000

    num_list = []
    stack = []
    num = 0
    # print(f'n // 3 = {n // 3}')
    # num_list.append(n // num)
    # print(f'num_list = {num_list}')

    for i in range(1, 10001):
        num += i
        stack.append(i)
        if num == n:
            break
        else:
            stack.pop()
    
    print(f'stack = {stack}')

    # if sum(num_list) == n:
    #     answer += 1
'''