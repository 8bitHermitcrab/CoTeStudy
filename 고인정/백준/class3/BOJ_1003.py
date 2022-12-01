# 피보나치 함수

'''
def fibonacci(n):
    if n == 0:
        print('0')
        return 0
    elif n == 1:
        print('1')
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(2))
'''


zero_cnt = [1, 0, 1]
one_cnt = [0, 1, 1]


# 테스트 케이스
t = int(input())

def solution(num):
    # length = 3
    length = len(zero_cnt)
    if length <= num:
        for i in range(length, num+1):
            zero_cnt.append(zero_cnt[i-1] + zero_cnt[i-2])
            one_cnt.append(one_cnt[i-1] + one_cnt[i-2])
    print(zero_cnt[num], one_cnt[num])

for _ in range(t):
    k = int(input())
    solution(k)

# https://doorbw.tistory.com/58