# 짝수 홀수

def solution(num):
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'

    return answer

    # 별찍기

a, b = map(int, input().strip().split(' '))

for i in range(b):

    for j in range(a):
        print('*', end='')

    print('')