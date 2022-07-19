# N개의 최소공배수

arr = [2,6,8,14]

# 최대공약수 GCD
def GCD(x, y):
    while y:
        # y를 x에 대입
        # x를 y로 나눈 나머지를 y에 대입
        x, y = y, x % y
    return x

# 최소공배수 LCM
def LCM(x, y):
    return (x * y) // GCD(x, y)

def solution(arr):
    # answer = 0

    while True:
        arr.append(LCM(arr.pop(), arr.pop()))
        # print(f'arr = {arr}')
        if len(arr) == 1:
            return arr[0]

    # return answer

print(solution(arr))


# https://brownbears.tistory.com/454