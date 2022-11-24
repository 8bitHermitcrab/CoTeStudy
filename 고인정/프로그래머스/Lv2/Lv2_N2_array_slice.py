# n^2 배열 자르기

n = 3
left = 2
right = 5

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        a = i // n
        b = i % n
        if a < b:
            a, b = b, a
        answer.append(a+1)
    return answer

print(solution(n, left, right))

# https://velog.io/@hannahf97/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-n2-%EB%B0%B0%EC%97%B4-%EC%9E%90%EB%A5%B4%EA%B8%B0

'''
# 3행 3열 2차원 배열
# i = 1, 2, 3
def solution(n, left, right):
    answer = []

    # arr[2], arr[2+1], ... , arr[5]
    
    # 1
    # arr = [1]
    # 2
    # arr = [1, 2, 2, 2]
    # 3
    # arr = [1, 2, 3, 2, 2, 3, 3, 3, 3]
    # 4
    # arr = [1, 2, 3, 4, 2, 2, 3, 4, 3, 3, 3, 4, 4, 4, 4, 4]
    # 5
    # arr = [1, 2, 3, 4, 5, ]
    # 6
    # arr = [1, 2, 3, 4, 5, 6]

    max_len = n**2
    # print(max_len)
    arr = []

    print(len(arr))

    # n이 5일 때
    while len(arr) < max_len:
        # 12345
        if len(arr) < n:
        for i in range(1, n+1):
            arr.append(i)
        # 22345
        for j in range()
        # 33345

        # 44445

        # 55555
    
    print(arr)

    
    return answer

print(solution(n, left, right))
'''

# 2x3행렬
# [ 
#  [1, 2, 3],
#  [4, 5, 6]
# ]