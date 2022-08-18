# 줄 서는 방법

n = 3
k = 5

import math

def solution(n, k):
    answer = []
    # n명의 사람 [1, 2, 3]
    nums = list(range(1, n+1))

    while k > 1:
        first = math.factorial(len(nums)-1)
        answer.append(nums.pop((k-1)//first))
        k = k - (first * ((k-1) // first))

    return answer + nums

# https://9yeah.tistory.com/8

'''
def solution(n, k):
    answer = []
    nums = [i for i in range(1, n+1)]

    while n != 0:
        # 줄 설 수 있는 총 방법은 n!
        # n! // n 을 하면 각 몇 번의 방법이 있는지 나옴
    
        # 한 사람이 앞에 줄섰을 때 경우의 수
        first = math.factorial(n) // n

     
        # k번째를 구하기 위해 한 사람이 앞에 줄섰을 때 경우의 수를 지나간 수
        passed = k // first
        
        # 나머지를 k에 넣기
        k = k % first
        
        if k == 0:
            answer.append(nums.pop(passed-1))

        else:
            answer.append(nums.pop(passed))
        
        n -= 1
        
    return answer



'''



'''
import math

def solution(n, k):
    answer = []
    n_list = [i for i in range(1, n+1)]

    while n != 0:
        print('------------------------')
        # 줄 설 수 있는 총 방법은 n!
        # n! // n 을 하면 각 몇 번의 방법이 있는지 나옴
        # 3! // 3 == 2
        print(f'n = {n}')
        print(f'temp = math.factorial(n)({math.factorial(n)}) // n({n}) == {math.factorial(n) // n}')
        # 한 사람이 앞에 줄섰을 때 경우의 수
        temp = math.factorial(n) // n

        # 5 // 2 == 2
        print(f' idx = k({k}) // temp({temp}) == {k // temp}')
        # k번째를 구하기 위해 한 사람이 앞에 줄섰을 때 경우의 수를 지나간 수
        idx = k // temp
        
        # 5 % 2 == 1
        print(f'k = k({k}) % temp({temp}) = {k % temp}')
        # 나머지를 k에 넣기
        k = k % temp
        
        if k == 0:
            print(f'n_list = {n_list}')
            print(f'n_list[idx-1] = n_list[{idx-1}]')
            print(f'answer0 = {answer}')
            answer.append(n_list.pop(idx-1))
            print(f'answer1 = {answer}')
        else:
            print(f'n_list = {n_list}')
            print(f'n_list[idx] = n_list[{idx}]')
            print(f'answer2 = {answer}')
            answer.append(n_list.pop(idx))
            print(f'answer3 = {answer}')
        
        n -= 1
        
    return answer

print(solution(n, k))


# https://velog.io/@ansrjsdn/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level3-%EC%A4%84-%EC%84%9C%EB%8A%94-%EB%B0%A9%EB%B2%95-Python


# https://greedysiru.tistory.com/519
'''