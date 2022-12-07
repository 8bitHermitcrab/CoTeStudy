# 이친수

# 0 : 0 개
# 1 => 1 : 1개
# 2 => 10 : 1개
# 3 => 100, 101 : 2개
# 4 => 1000, 1010, 1001 : 3개
# 5 => 10000, 10100, 10101, 10100, 10010, 10001 : 5개
# 6 => 100000, 101010, 100101, 100010, 101001, 101000, 100100, 100001 : 8개

n = int(input())

dp = [0, 1, 1]

for i in range(3, 91):
    answer = dp[i-1] + dp[i-2]
    dp.append(answer)

print(dp[n])


# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-2193%EB%B2%88-%EC%9D%B4%EC%B9%9C%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

'''
# n = int(input())
# cnt = 0

# 이진수
def binaryNum(x):
    num = str(bin(x))
    return num[2:]

# 이친수
def pinaryNum(y):
    num = y.replace('11', '*')
    if '*' in num:
        return False
    else:
        return True

for i in range(1, 99999999999999):
    k = binaryNum(i)
    if len(k) == n:
        num = pinaryNum(k)
        if num == True:
            cnt += 1

print(cnt)

# print(bin(2))

'''