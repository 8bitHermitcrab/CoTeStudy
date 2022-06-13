# 약수의 개수와 덧셈

left = 13
right = 17


answer = 0
temp = []
cnt = 0

# left~right
for i in range(left, right+1):
    # 약수 구하기
    for j in range(1, i+1):
        if i % j == 0:
            temp.append(j)
            cnt = len(temp)
    temp = []

    if cnt % 2 == 0:
        answer += i
    else:
        answer -= i