# 요세푸스 문제 0

n, k = map(int, input().split())

# 원
circle = [i for i in range(1, n+1)]

# 원을 도는 주기
cycle = k - 1

answer = []

for i in range(n):
    if len(circle) > cycle:
        answer.append(circle.pop(cycle))
        cycle += (k-1)
    elif len(circle) <= cycle:
        cycle = cycle % len(circle)
        answer.append(circle.pop(cycle))
        cycle += (k-1)

print('<', ', '.join(str(i) for i in answer), '>', sep='')

# https://tturbo0824.tistory.com/18

'''
# 제거된 사람들을 넣을 배열
answer = []
# 제거된 사람들 인덱스 번호
idx = 0

for i in range(n):
    idx += (k-1) 

    if idx >= len(circle):
        print(f'idx = {idx}')
        print(f'len(circle) = {len(circle)}')
        idx = idx % len(circle)
        print(f'idx % len(circle) = {idx % len(circle)}')

    answer.append(str(circle.pop(idx)))
    print(f'answer = {answer}')

print('<', ', '.join(answer), '>', sep='')
'''

# https://infinitt.tistory.com/213


# https://hongcoding.tistory.com/41



# print(circle)

# [0 1 2 3 4 5 6]
# 1 2 '3' 4 5 6 7 
#         4 5 '6' 7 1 2
#                 7 1 '2' 3 4 5 6
#                         3 4 5 6 7 1 2 
#

# 앞 = [:k-1]
# 뒤 = k번째 리스트 = [k:]

# 3, 6, 2...
'''num = 0
while num != n:
    print(f'num = {num}')
    print(f'circle[:k-1] = {circle[:k-1]}')
    print(f'circle[k:] = {circle[k:]}')
    temp = circle[k-1]
    print(f'temp = {temp}')
    front = circle[:k-1]
    behind = circle[k:]
    answer.append(temp)

    circle = behind + front
    circle.append(temp)

    print(f'circle = {circle}')
    print(f'answer = {answer}')
    num += 1

print(answer)'''