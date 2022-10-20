# 점프와 순간 이동

# n = 5
# n = 6
n = 5000

# 거꾸로 2로 나눠가면서 구한다.
# 2로 안 나누어진다면, 점프가 필요해서 건전지 사용량이 +1

def solution(n):
    answer = 0
    
    while n > 0:
        # print(f'n = {n}')
        # print(f'{n} % 2 = {n % 2}')
        answer += n % 2
        # print(f'answer = {answer}')
        # print(f'{n}//=2 = {n // 2}')
        n //= 2
    return answer

print(solution(n))

# https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EC%A0%90%ED%94%84%EC%99%80-%EC%88%9C%EA%B0%84-%EC%9D%B4%EB%8F%99

'''
def solution(n):
    ans = 0

    # k칸 점프 - 배터리 k
    # 현재까지 온 거리 * 2
    # 건전지 사용량 최솟값 ans    
    # 0 1 2 3 4 5 6
    space = 0
    jump = 1
    k = jump * 2 # 2
    space = 2
    jump = 1
    space = jump + k # 3

    k = 3

    return ans

print(solution(n))
'''