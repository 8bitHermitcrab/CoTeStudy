# 수 찾기

import sys

n = int(sys.stdin.readline())
n_set = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    if i in n_set:
        print(1)
    else:
        print(0)



# n_list.sort()

'''for i in m_list:
    left, right = 0, n-1
    isExist = False

    # 이분탐색
    # left가 right보다 커지면 반복문 탈출
    while left <= right:
        # 중간값
        mid = (left + right) // 2
        if i == n_list[mid]:
            isExist = True
            print(1)
            break
        elif i > n_list[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if not isExist:
        print(0)'''
# https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-1920%EB%B2%88-%EC%88%98-%EC%B0%BE%EA%B8%B0-Python

'''print(n_list)
print(m_list)

answer = []
for i in m_list:
    if i in n_list:
        answer.append(1)
    else:
        answer.append(0)

print(answer)

for i in answer:
    print(i)
'''

# https://chancoding.tistory.com/44