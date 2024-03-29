#220919
# 1. x가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. x가 2로 나누어 떨어지면, 2로 나눈다
# 3. 1을 뺀다

#3개를 적절히 사용해서 1을 만드는 연산 횟수의 최솟값 구하기

#-----------------틀림----------------------------#
# #입력
# x = int(input())

# #횟수
# cnt = 0

# while x !=1:
#     if x % 3 == 0:
#         x = x/3
#         cnt += 1
#     elif x % 2 == 0:
#         x = x/2
#         cnt += 1
#     else:
#         x = x-1
#         cnt += 1

# print(cnt)


# https://latte-is-horse.tistory.com/201
# DP 사용

x = int(input())

# dp 테이블
# 입력 <= 10^6이기 때문에
d = [0] * 1000001 # (0 포함)


#d[1] = 0
#d[2] = 1
#d[3] = 1
#d[4] = 2   4 -> 2 -> 1 (2 -> 1 = d[2])
#d[6] = 2
#d[11] = 4

#d[12] = 3 (12는 2와 3으로 나누어 떨어짐)
# -> d[11]+1 = 5, d[6]+1 = 3, d[4]+1 = 3 
# -> 12 전 숫자, 2로 나누어 떨어진거, 3으로 나누어 떨어진거

#따라서,
#d[n]은 d[n-1], 2로 나누어 떨어지면 d[n//2], 3으로 나누어 떨어지면 d[n//3]
#에 각각 1씩 더한것 들 중 최솟값

for i in range(2, x+1):
    #d[n-1]의 경우
    lst = [d[i-1]]
    print(i)
    print(lst)

    #3으로 나누어 떨어질 때의 경우 추가하기
    if i % 3 == 0:
        lst.append(d[i//3])
    #2로 나누어 떨어질 때의 경우 추가하기
    if i % 2 == 0:
        lst.append(d[i//2])
    print(lst)
    d[i] = min(lst) + 1

print(d[x])