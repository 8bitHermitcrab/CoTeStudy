# 1, 2, 3 더하기

# 1 -> 1가지
# 2 = 1+1, 2 -> 2가지
# 3 = 1+1+1, 2+1, 1+2, 3 -> 4가지
# 4 -> 7가지
# 5
# 6
# 7 -> 44가지

# 점화식
# f(n) = f(n-1) + f(n-2) + f(n+3)

t = int(input())

for i in range(t):
    num = int(input())
    result_list = [0] * (num+1)

    if num == 1:
        print(1)
    elif num == 2:
        print(2)
    elif num == 3:
        print(4)
    else:
        result_list[1] = 1
        result_list[2] = 2
        result_list[3] = 4
        for j in range(4, num+1):
            result_list[j] = result_list[j-1] + result_list[j-2] + result_list[j-3]
        print(result_list[num])
    

print(result_list)

# https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-9095-123-%EB%8D%94%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python



'''
# 테스트 케이스
# t = int(input())

# sum_list = []

# for _ in range(t):
#     sum_list.append(int(input()))

# result_list = []

cnt = 0

def count_sum(num):
    cnt = 0
    for i in range(len(sum_list)):
        temp = sum_list[i]
        while temp > 0:
            temp -= 1

        if temp == 0:
            cnt += 1

    return cnt 

print(count_sum(4))
'''