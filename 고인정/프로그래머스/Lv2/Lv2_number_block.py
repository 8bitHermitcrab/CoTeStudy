# 숫자 블록

begin = 1
end = 10

import math

def solution(begin, end):
    answer = []
    
    for i in range(begin, end+1):
        print(f'i = {i}')
        if i == 1:
            answer.append(0)
        else:
            # i의 약수 중(1 제외) 가장 작은 수로 나눈 몫이 해당 인덱스의 값이 됨
            # 10//5 == 5 : 2, 5, 10
            # 9//3 == 3 : 3, 9
            # 7//7 == 1 
            # 소수가 아니면 몫, 소수이면 1
            sqrt = int(math.sqrt(i))
            print(f'sqrt = {sqrt}')
            
            for j in range(2, sqrt+1):
                print(f'j = {j}')

                # 몫 : quotient
                q = i // j
                print(f'q = {q}')

                # # 10,000,000번 블록까지
                if q > 10 ** 7:
                    continue
                if i % j == 0:
                    answer.append(q)
                    break

            else:
                answer.append(1)
  
    return answer


print(solution(begin, end))


# https://deok2kim.tistory.com/123